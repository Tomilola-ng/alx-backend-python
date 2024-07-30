#!/usr/bin/env python3
"""Unit testing module for the GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Ensure that GithubOrgClient.org fetches the correct data."""
        client_instance = GithubOrgClient(org_name)
        client_instance.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """Test the _public_repos_url property of GithubOrgClient."""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "http://example.com/repos"}
            mock_org.return_value = payload
            client_instance = GithubOrgClient('test')
            self.assertEqual(
                client_instance._public_repos_url,
                payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""
        json_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = json_payload

        #pylint: disable=line-too-long
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "http://example.com/repos"
            client_instance = GithubOrgClient('test')
            result = client_instance.public_repos()
