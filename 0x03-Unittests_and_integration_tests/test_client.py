#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, call
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, {})

    @patch('client.GithubOrgClient.org', return_value={"payload": True})
    def test_public_repos_url(self, mock_org):
        client = GithubOrgClient("test_org")
        result = client._public_repos_url
        mock_org.assert_called_once()
        self.assertEqual(result, {"payload": True}["repos_url"])

    @patch('client.get_json', return_value=[{"name": "repo1"}, {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/repos/test_org/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        client = GithubOrgClient("test_org")
        result = client.public_repos()
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/repos/test_org/repos")
        self.assertEqual(result, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

@parameterized_class("org_payload", "repos_payload", "expected_repos", "apache2_repos")
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self):
        self.mock_get.side_effect = [
            Mock(json=lambda: self.org_payload),
            Mock(json=lambda: self.repos_payload),
        ]

    def tearDown(self):
        self.mock_get.reset_mock()

    def test_public_repos_integration(self):
        client = GithubOrgClient("test_org")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

        self.mock_get.assert_has_calls([
            call(f"https://api.github.com/orgs/test_org"),
            call(f"https://api.github.com/orgs/test_org/repos"),
        ])

if __name__ == '__main__':
    unittest.main()
