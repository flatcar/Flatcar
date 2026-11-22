#!/usr/bin/env python3
import io
import json
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Add parent directory to sys.path if needed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fetch_active_repos


class TestFetchActiveRepos(unittest.TestCase):

    @patch("urllib.request.urlopen")
    def test_fetch_repos_from_api_filters_archived_and_forks(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.headers.get.return_value = ""
        mock_data = [
            {"full_name": "flatcar/repo1", "archived": False, "fork": False},
            {"full_name": "flatcar/archived-repo", "archived": True, "fork": False},
            {"full_name": "flatcar/fork-repo", "archived": False, "fork": True},
            {"full_name": "flatcar/repo2", "archived": False, "fork": False},
        ]
        mock_response.read.return_value = json.dumps(mock_data).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        repos = fetch_active_repos.fetch_repos_from_api(token="fake_token")
        self.assertEqual(repos, ["flatcar/repo1", "flatcar/repo2"])

    @patch("urllib.request.urlopen")
    def test_fetch_repos_from_api_error_returns_none(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("API connection error")
        repos = fetch_active_repos.fetch_repos_from_api(token="fake_token")
        self.assertIsNone(repos)

    def test_fetch_repos_from_maintainers(self):
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write("""
| subgroup | repos |
| --- | --- |
| group | [nebraska](https://github.com/flatcar/nebraska)<br>[go-omaha](https://github.com/flatcar/go-omaha) |
""")
            tmp_path = tmp.name

        try:
            repos = fetch_active_repos.fetch_repos_from_maintainers(maintainers_file=tmp_path)
            self.assertIn("flatcar/nebraska", repos)
            self.assertIn("flatcar/go-omaha", repos)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    @patch("fetch_active_repos.fetch_repos_from_api")
    def test_main_with_github_env(self, mock_fetch_api):
        mock_fetch_api.return_value = ["flatcar/repo1", "flatcar/repo2"]
        with tempfile.NamedTemporaryFile("w+", delete=False) as env_tmp:
            env_path = env_tmp.name

        try:
            with patch.dict(os.environ, {"GITHUB_ENV": env_path}):
                fetch_active_repos.main()

            with open(env_path, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn("REPOSITORIES=flatcar/repo1,flatcar/repo2", content)
        finally:
            if os.path.exists(env_path):
                os.remove(env_path)


if __name__ == "__main__":
    unittest.main()
