#!/usr/bin/env python3
"""
Fetch active (non-archived, non-fork) repositories from the flatcar GitHub organization.
Falls back to parsing MAINTAINERS.md if API calls fail or return no results.
Exports result to GITHUB_ENV as REPOSITORIES="flatcar/repo1,flatcar/repo2,...".
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request


def fetch_repos_from_api(token=None, org="flatcar"):
    """
    Fetch all active, non-archived, non-fork repos for an org via GitHub REST API.
    """
    repos = []
    page = 1
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "flatcar-contrib-metrics",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    while True:
        url = f"https://api.github.com/orgs/{org}/repos?type=public&per_page=100&page={page}"
        req = urllib.request.Request(url, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                if response.status != 200:
                    break
                data = json.loads(response.read().decode("utf-8"))
                if not data:
                    break
                for repo in data:
                    if not repo.get("archived", False) and not repo.get("fork", False):
                        full_name = repo.get("full_name")
                        if full_name and full_name not in repos:
                            repos.append(full_name)
                
                link_header = response.headers.get("Link", "")
                if 'rel="next"' not in link_header and len(data) < 100:
                    break
                page += 1
        except Exception as err:
            print(f"Warning: GitHub API request failed: {err}", file=sys.stderr)
            return None

    return repos


def fetch_repos_from_maintainers(maintainers_file="MAINTAINERS.md"):
    """
    Fallback method: parse repo names from MAINTAINERS.md.
    """
    if not os.path.exists(maintainers_file):
        return []

    repos = []
    pattern = re.compile(r"github\.com/flatcar/([a-zA-Z0-9_\-\.]+)")
    try:
        with open(maintainers_file, "r", encoding="utf-8") as f:
            content = f.read()
            matches = pattern.findall(content)
            for repo in matches:
                # Remove trailing anchor or file extensions if present
                clean_repo = repo.rstrip(")")
                full_name = f"flatcar/{clean_repo}"
                if full_name not in repos:
                    repos.append(full_name)
    except Exception as err:
        print(f"Warning: Failed to read {maintainers_file}: {err}", file=sys.stderr)

    return repos


def main():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    repos = fetch_repos_from_api(token=token)

    if not repos:
        print("Falling back to MAINTAINERS.md for repository list...", file=sys.stderr)
        repos = fetch_repos_from_maintainers()

    if not repos:
        print("Error: Could not retrieve repository list from API or MAINTAINERS.md", file=sys.stderr)
        sys.exit(1)

    repo_str = ",".join(repos)
    print(f"Discovered {len(repos)} active repositories.")

    github_env = os.environ.get("GITHUB_ENV")
    if github_env:
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"REPOSITORIES={repo_str}\n")
        print(f"Exported REPOSITORIES to {github_env}")
    else:
        print(f"REPOSITORIES={repo_str}")


if __name__ == "__main__":
    main()
