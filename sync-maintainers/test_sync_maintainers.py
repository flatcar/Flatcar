import importlib.util
import os
import sys
import unittest
from unittest.mock import MagicMock, call, mock_open, patch

# Add sync-maintainers directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

spec = importlib.util.spec_from_file_location(
    "sync_maintainers",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "sync-maintainers.py"),
)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class TestSyncMaintainers(unittest.TestCase):

    def test_parse(self):
        sample_lines = [
            "# Maintainers",
            "General governance paragraph line 1.",
            "General governance paragraph line 2.",
            "### nebraska",
            "maintainers:",
            "* [@t-lo](https://github.com/t-lo)",
            "* [@pothos](https://github.com/pothos)",
            "### Flatcar",
            "maintainers:",
            "* [@chewi](https://github.com/chewi)",
        ]
        para, repos = sync.parse(sample_lines)
        self.assertEqual(
            para,
            [
                "General governance paragraph line 1.",
                "General governance paragraph line 2.",
            ],
        )
        self.assertEqual(len(repos), 1)
        self.assertEqual(repos[0][0], "nebraska")
        self.assertEqual(
            repos[0][1],
            [
                "* [@t-lo](https://github.com/t-lo)",
                "* [@pothos](https://github.com/pothos)",
            ],
        )

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="# Maintainers\nIntro text\n### repo1\nmaintainers:\n* [@user1](https://github.com/user1)\n",
    )
    def test_parse_maintainers(self, mock_file):
        repos, paragraph = sync.parse_maintainers(maint_file="dummy_MAINTAINERS.md")
        self.assertEqual(paragraph, "Intro text")
        self.assertEqual(len(repos), 1)
        self.assertEqual(repos[0][0], "repo1")

    def test_prepare_req_header_formatting(self):
        url, headers = sync.prepare_req("nebraska", "my-secret-token", "pulls")
        self.assertEqual(url, "https://api.github.com/repos/flatcar/nebraska/pulls")
        self.assertEqual(headers["Authorization"], "Bearer my-secret-token")
        self.assertNotIn("{token}", headers["Authorization"])

    def test_get_assignees(self):
        maintainers = [
            "* [@t-lo](https://github.com/t-lo)",
            "* [@pothos](https://github.com/pothos)",
        ]
        assignees = sync.get_assignees(maintainers)
        self.assertEqual(assignees, ["t-lo", "pothos"])

    @patch("subprocess.run")
    def test_clone_repo_ssh_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        sync.clone_repo("nebraska")
        mock_run.assert_called_once_with(
            ["git", "clone", "--depth=1", "git@github.com:flatcar/nebraska"], check=True
        )

    @patch("subprocess.run")
    def test_clone_repo_ssh_fail_https_fallback(self, mock_run):
        import subprocess

        def run_side_effect(cmd, check=True):
            if "git@github.com" in cmd[3]:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0)

        mock_run.side_effect = run_side_effect
        sync.clone_repo("nebraska")
        self.assertEqual(mock_run.call_count, 2)
        mock_run.assert_has_calls(
            [
                call(
                    ["git", "clone", "--depth=1", "git@github.com:flatcar/nebraska"],
                    check=True,
                ),
                call(
                    [
                        "git",
                        "clone",
                        "--depth=1",
                        "https://github.com/flatcar/nebraska.git",
                    ],
                    check=True,
                ),
            ]
        )

    @patch.object(sync, "parse_maintainers")
    @patch("subprocess.run")
    def test_dry_run_repo(self, mock_subproc, mock_parse):
        mock_parse.return_value = (
            [("nebraska", ["* [@t-lo](https://github.com/t-lo)"])],
            "para",
        )
        args = MagicMock(dry_run=True, repo="nebraska")
        sync.main_repo(args)
        mock_subproc.assert_not_called()

    @patch.object(sync, "parse_maintainers")
    @patch.object(sync, "get_session")
    def test_dry_run_github(self, mock_get_session, mock_parse):
        mock_parse.return_value = (
            [("nebraska", ["* [@t-lo](https://github.com/t-lo)"])],
            "para",
        )
        args = MagicMock(dry_run=True, repo="nebraska")
        sync.main_github(args)
        mock_get_session.assert_not_called()


if __name__ == "__main__":
    unittest.main()
