#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def get_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def parse(m):
    para = []
    repos = []
    while len(m):
        line = m.pop(0)
        if line == "# Maintainers":
            line = m.pop(0)
            while not line.startswith("#"):
                para.append(line)
                line = m.pop(0)
        if line.startswith("###"):
            repo = line.split("### ")[1].strip()
            maint = []
            m.pop(0)  # maintainers:
            line = m.pop(0)
            while line.startswith("* "):
                maint.append(line)
                line = m.pop(0) if len(m) else ""
            if repo != "Flatcar":
                repos.append((repo, maint))
    return para, repos


MAINTAINERS_TEMPLATE = """# Maintainers

{maintainers}

{paragraph}

The contents of this file are synchronized from [Flatcar/MAINTAINERS.md](https://github.com/flatcar/Flatcar/blob/main/MAINTAINERS.md).
"""


def write_maintainers_file(repo_name, paragraph, maintainers):
    maintainers_entry = "\n".join(maintainers)
    maintainers_content = MAINTAINERS_TEMPLATE.format(
        maintainers=maintainers_entry, paragraph=paragraph
    )
    repo_filename = f"{repo_name}/MAINTAINERS.md"
    with open(repo_filename, "w") as f:
        f.write(maintainers_content)


BRANCH_NAME = "sync-maintainers"


def clone_repo(repo_name):
    ssh_url = f"git@github.com:flatcar/{repo_name}"
    https_url = f"https://github.com/flatcar/{repo_name}.git"
    try:
        subprocess.run(["git", "clone", "--depth=1", ssh_url], check=True)
    except subprocess.CalledProcessError:
        print(f"SSH clone failed for {repo_name}, falling back to HTTPS...")
        subprocess.run(["git", "clone", "--depth=1", https_url], check=True)


def checkout_branch(repo_name):
    return subprocess.run(
        ["git", "-C", repo_name, "checkout", "-B", BRANCH_NAME, "origin/HEAD"],
        check=True,
    )


def commit(repo_name):
    subprocess.run(["git", "-C", repo_name, "add", "MAINTAINERS.md"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            repo_name,
            "commit",
            "-m",
            "Sync maintainers file from flatcar/flatcar repository",
        ],
        check=True,
    )


def push(repo_name):
    subprocess.run(
        ["git", "-C", repo_name, "push", "--force", "origin", BRANCH_NAME], check=True
    )


def parse_maintainers(repo=None, maint_file="../MAINTAINERS.md"):
    if not os.path.isabs(maint_file) and not os.path.exists(maint_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        candidates = [
            os.path.join(script_dir, maint_file),
            "MAINTAINERS.md",
            os.path.join(script_dir, "..", "MAINTAINERS.md"),
        ]
        for candidate in candidates:
            if os.path.exists(candidate):
                maint_file = candidate
                break
    with open(maint_file) as f:
        m = f.read().splitlines()
    para, repos = parse(m)
    paragraph = "\n".join(para).strip()
    if repo:
        repos = [r for r in repos if r[0] == repo]
    return repos, paragraph


def main_repo(args):
    repos, paragraph = parse_maintainers(args.repo)
    for repo_name, maintainers in repos:
        if args.dry_run:
            print(
                f"[DRY-RUN] Would clone repo {repo_name}, checkout {BRANCH_NAME}, "
                f"write MAINTAINERS.md, commit, and push"
            )
            continue
        clone_repo(repo_name)
        checkout_branch(repo_name)
        write_maintainers_file(repo_name, paragraph, maintainers)
        commit(repo_name)
        push(repo_name)


def prepare_req(repo, token, api):
    api = "/" + api if api else ""
    url = f"https://api.github.com/repos/flatcar/{repo}{api}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    return url, headers


def get_pr(repo, token, session=None):
    if session is None:
        session = get_session()
    url, headers = prepare_req(repo, token, "pulls")
    params = {"state": "open", "head": f"flatcar:{BRANCH_NAME}"}
    return session.get(url, headers=headers, params=params)


def get_default_branch(repo, token, session=None):
    if session is None:
        session = get_session()
    url, headers = prepare_req(repo, token, "")
    resp = session.get(url, headers=headers).json()
    return resp["default_branch"]


def create_pr(repo, token, base, session=None):
    if session is None:
        session = get_session()
    url, headers = prepare_req(repo, token, "pulls")
    data = {
        "title": "Sync MAINTAINERS.md",
        "head": f"flatcar:{BRANCH_NAME}",
        "base": base,
    }
    return session.post(url, headers=headers, json=data)


def update_assignees(repo, token, pr, assignees, session=None):
    if session is None:
        session = get_session()
    url, headers = prepare_req(repo, token, f"pulls/{pr}/requested_reviewers")
    data = {"reviewers": assignees}
    return session.post(url, headers=headers, json=data)


def get_assignees(maintainers):
    assignees = []
    for e in maintainers:
        if "@" in e:
            handle = e.split("@")[1].split("]")[0].strip()
            if handle:
                assignees.append(handle)
    return assignees


def main_github(args):
    token = os.getenv("GITHUB_TOKEN")
    if not token and not args.dry_run:
        raise Exception("Missing GITHUB_TOKEN env variable")
    if not token:
        token = "dry_run_token"
    repos, _ = parse_maintainers(args.repo)
    session = None
    for repo_name, maintainers in repos:
        assignees = get_assignees(maintainers)
        if args.dry_run:
            print(
                f"[DRY-RUN] Would check/create PR for {repo_name} and request reviewers: {assignees}"
            )
            continue
        if session is None:
            session = get_session()
        pr_resp = get_pr(repo_name, token, session=session)
        pr = pr_resp.json()
        if not pr:
            print(f"{repo_name} creating pr")
            base = get_default_branch(repo_name, token, session=session)
            pr = [create_pr(repo_name, token, base, session=session).json()]
        prnum = pr[0]["number"]
        resp = update_assignees(repo_name, token, prnum, assignees, session=session)
        if resp.status_code != 201:
            print(resp.json())
        else:
            print(f"{repo_name} ok")


def main_list(args):
    repos, _ = parse_maintainers()
    for repo_name, _ in repos:
        print(repo_name)


parser = argparse.ArgumentParser(prog="sync-maintainers.py")
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview actions without modifying git repositories or sending GitHub REST API POST requests",
)
subparser = parser.add_subparsers(required=True, dest="cmd")
parser_repo = subparser.add_parser("repo", help="perform git repository operations")
parser_repo.add_argument("--repo", help="Repository to operate on; default all")
parser_repo.set_defaults(func=main_repo)
parser_github = subparser.add_parser(
    "github", help="perform github pull request operations"
)
parser_github.add_argument("--repo", help="Repository to operate on; default all")
parser_github.set_defaults(func=main_github)
parser_list = subparser.add_parser("list", help="list all repositories with entries")
parser_list.set_defaults(func=main_list)

if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
