#!/usr/bin/env python3
import importlib.util
import io
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Import sync-maintainers.py using importlib since filename contains a hyphen
spec = importlib.util.spec_from_file_location(
    "sync_maintainers",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "sync-maintainers.py"),
)
sync_maintainers = importlib.util.module_from_spec(spec)
sys.modules["sync_maintainers"] = sync_maintainers
spec.loader.exec_module(sync_maintainers)

SAMPLE_MAINTAINERS_MD = """# Maintainers

See Governance for details.

## Flatcar Maintainers

| Name | GitHub |
| --- | --- |
| Person | [@person](https://github.com/person) |

## Maintainer Subgroups

Subgroups are teams of maintainers.

| Subgroup | Description | Members | Repositories |
| --- | --- | --- | --- |
| **test-maintainers** | Reviews test items | [@t-lo](https://github.com/t-lo)<br>[@pothos](https://github.com/pothos) | [nebraska](https://github.com/flatcar/nebraska)<br>[go-omaha](https://github.com/flatcar/go-omaha) |
| **core-maintainers** | Reviews Core | [@chewi](https://github.com/chewi) | [Flatcar](https://github.com/flatcar/Flatcar)<br>[mantle](https://github.com/flatcar/mantle) |
"""


class TestSyncMaintainers(unittest.TestCase):
    def test_parse_table(self):
        lines = SAMPLE_MAINTAINERS_MD.splitlines()
        para, repos = sync_maintainers.parse(lines)
        
        # Verify paragraph extraction
        paragraph = "\n".join(para).strip()
        self.assertIn("See Governance for details.", paragraph)

        # Convert repos list of tuples to a dict for easy checking
        repos_dict = dict(repos)

        # Verify repos mapped correctly with bulleted usernames
        self.assertIn("nebraska", repos_dict)
        self.assertEqual(repos_dict["nebraska"], ["* @t-lo", "* @pothos"])

        self.assertIn("go-omaha", repos_dict)
        self.assertEqual(repos_dict["go-omaha"], ["* @t-lo", "* @pothos"])

        self.assertIn("mantle", repos_dict)
        self.assertEqual(repos_dict["mantle"], ["* @chewi"])

        # Ensure 'Flatcar' repository itself is ignored
        self.assertNotIn("Flatcar", repos_dict)

    def test_prepare_req_authorization_header(self):
        repo = "nebraska"
        token = "test_secret_token_123"
        url, headers = sync_maintainers.prepare_req(repo, token, "pulls")

        self.assertEqual(url, "https://api.github.com/repos/flatcar/nebraska/pulls")
        self.assertEqual(headers["Accept"], "application/vnd.github+json")
        # Ensure token is interpolated correctly into value, not key
        self.assertEqual(headers.get("Authorization"), "Bearer test_secret_token_123")
        self.assertNotIn("Bearer {token}", headers.values())

    def test_get_assignees(self):
        maintainers = ["* @t-lo", "* @pothos", "* @jepio"]
        assignees = sync_maintainers.get_assignees(maintainers)
        self.assertEqual(assignees, ["t-lo", "pothos", "jepio"])

    @patch("sync_maintainers.update_assignees")
    @patch("sync_maintainers.get_pr")
    @patch("sync_maintainers.parse_maintainers")
    def test_main_github_print_formatting(self, mock_parse, mock_get_pr, mock_update):
        mock_parse.return_value = ([("nebraska", ["* @t-lo"])], "sample para")
        
        mock_pr_resp = MagicMock()
        mock_pr_resp.json.return_value = [{"number": 42}]
        mock_get_pr.return_value = mock_pr_resp

        mock_update_resp = MagicMock()
        mock_update_resp.status_code = 201
        mock_update.return_value = mock_update_resp

        with patch.dict(os.environ, {"GITHUB_TOKEN": "fake_token"}):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                sync_maintainers.main_github(MagicMock(repo="nebraska"))
                output = mock_stdout.getvalue().strip()
                # Confirm it prints actual repo name rather than "{repo_name} ok" literal
                self.assertEqual(output, "nebraska ok")
                self.assertNotEqual(output, "{repo_name} ok")


if __name__ == "__main__":
    unittest.main()
