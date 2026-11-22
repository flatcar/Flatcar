#!/usr/bin/env python3
"""Regression tests for the date handling of the monthly contributor report.

The "Set the start and end dates" step of
``.github/workflows/issue-pr-contrib-metrics.yaml`` turns the
``workflow_dispatch`` inputs ``start_date`` / ``end_date`` into the
``START_DATE`` / ``END_DATE`` environment variables that every later step of
the workflow consumes.

Those inputs are supplied by a human when the workflow is dispatched, so they
must never be able to influence anything other than the value of the two
variables.  These tests therefore reproduce what the Actions runner does --
expand the ``${{ ... }}`` expressions of the step, then execute the resulting
``run`` block with bash -- and assert that hostile input neither executes
commands nor smuggles extra variables into ``$GITHUB_ENV``.

Run with::

    python3 .github/scripts/test_metrics_date_inputs.py
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKFLOW = os.path.join(REPO_ROOT, ".github", "workflows", "issue-pr-contrib-metrics.yaml")
JOB = "contributor_report"
STEP = "Set the start and end dates"

# Matches an Actions expression such as "${{ inputs.start_date }}" or
# "${{inputs.start_date}}" and captures the context path it refers to.
EXPRESSION = re.compile(r"\$\{\{\s*([A-Za-z0-9_.-]+)\s*\}\}")


def load_step():
    """Return the (env, run) pair of the date handling step."""
    with open(WORKFLOW, encoding="utf-8") as handle:
        workflow = yaml.safe_load(handle)

    for step in workflow["jobs"][JOB]["steps"]:
        if step.get("name") == STEP:
            return step.get("env") or {}, step["run"]

    raise AssertionError("step %r not found in %s" % (STEP, WORKFLOW))


def expand(text, inputs):
    """Expand Actions expressions the way the runner does, before bash runs.

    Only the ``inputs`` context is relevant here; any other context is
    irrelevant to this step and expands to the empty string, which is what the
    runner does for an unset input as well.
    """

    def replace(match):
        path = match.group(1)
        context, _, name = path.partition(".")
        if context == "inputs":
            return inputs.get(name, "")
        return ""

    return EXPRESSION.sub(replace, text)


def run_step(inputs, workdir):
    """Execute the date handling step with the given dispatch inputs.

    Returns the CompletedProcess and the parsed contents of $GITHUB_ENV.
    """
    step_env, run_block = load_step()

    env = {
        "PATH": os.environ["PATH"],
        "HOME": workdir,
        "GITHUB_ENV": os.path.join(workdir, "github_env"),
    }
    # Step-level `env:` values go through expression expansion too.
    for key, value in step_env.items():
        env[key] = expand(str(value), inputs)

    open(env["GITHUB_ENV"], "w", encoding="utf-8").close()

    script = os.path.join(workdir, "step.sh")
    with open(script, "w", encoding="utf-8") as handle:
        handle.write(expand(run_block, inputs))

    proc = subprocess.run(
        ["bash", script],
        cwd=workdir,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    exported = {}
    with open(env["GITHUB_ENV"], encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            name, _, value = line.partition("=")
            exported[name] = value

    return proc, exported


def has_gnu_date():
    """The scheduled fallback needs GNU date's `-d` option."""
    date = shutil.which("date")
    if date is None:
        return False
    proc = subprocess.run(
        [date, "--version"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        universal_newlines=True,
    )
    return proc.returncode == 0 and "GNU coreutils" in proc.stdout


class DateInputTest(unittest.TestCase):
    def setUp(self):
        self.workdir = tempfile.mkdtemp(prefix="metrics-date-test-")
        self.addCleanup(shutil.rmtree, self.workdir, True)

    def test_explicit_dates_are_used(self):
        """A well formed dispatch is passed through unchanged."""
        proc, exported = run_step(
            {"start_date": "2026-01-01", "end_date": "2026-01-31"}, self.workdir
        )

        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(exported.get("START_DATE"), "2026-01-01")
        self.assertEqual(exported.get("END_DATE"), "2026-01-31")

    def test_scheduled_run_falls_back_to_computed_dates(self):
        """Without inputs (the `schedule` trigger) dates are computed."""
        if not has_gnu_date():
            self.skipTest("GNU date is required for the scheduled fallback")

        proc, exported = run_step({}, self.workdir)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertRegex(exported.get("START_DATE", ""), r"^\d{4}-\d{2}-\d{2}$")
        self.assertRegex(exported.get("END_DATE", ""), r"^\d{4}-\d{2}-\d{2}$")

    def test_input_cannot_execute_commands(self):
        """A command substitution in an input must not be executed."""
        marker = os.path.join(self.workdir, "pwned.marker")
        payload = '$(touch "%s")2026-01-01' % marker

        proc, exported = run_step(
            {"start_date": payload, "end_date": "2026-01-31"}, self.workdir
        )

        self.assertFalse(
            os.path.exists(marker),
            "start_date was evaluated as shell code by the workflow step",
        )
        self.assertNotEqual(
            proc.returncode, 0, "a malformed start_date must fail the step"
        )
        self.assertNotIn("START_DATE", exported)

    def test_input_cannot_inject_extra_environment_variables(self):
        """A newline in an input must not add variables to $GITHUB_ENV."""
        payload = "2026-01-01\nPWNED=yes"

        proc, exported = run_step(
            {"start_date": payload, "end_date": "2026-01-31"}, self.workdir
        )

        self.assertNotIn(
            "PWNED", exported, "start_date smuggled an extra variable into $GITHUB_ENV"
        )
        self.assertNotEqual(
            proc.returncode, 0, "a malformed start_date must fail the step"
        )

    def test_end_date_is_validated_too(self):
        """end_date reaches the same sinks and gets the same treatment."""
        marker = os.path.join(self.workdir, "pwned-end.marker")
        payload = '$(touch "%s")2026-01-31' % marker

        proc, exported = run_step(
            {"start_date": "2026-01-01", "end_date": payload}, self.workdir
        )

        self.assertFalse(
            os.path.exists(marker),
            "end_date was evaluated as shell code by the workflow step",
        )
        self.assertNotEqual(
            proc.returncode, 0, "a malformed end_date must fail the step"
        )
        self.assertNotIn("END_DATE", exported)

    def test_partial_input_is_rejected(self):
        """Supplying only one of the two dates must not be silently ignored."""
        # Without GNU date the fallback branch fails on its own, which would
        # make this assertion pass for the wrong reason.
        if not has_gnu_date():
            self.skipTest("GNU date is required to tell this apart from the fallback")

        proc, exported = run_step({"start_date": "2026-01-01"}, self.workdir)

        self.assertNotEqual(
            proc.returncode, 0, "an incomplete date range must fail the step"
        )
        self.assertNotIn("START_DATE", exported)


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=False)
