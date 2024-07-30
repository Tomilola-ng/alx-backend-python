#!/usr/bin/env python3
'''Unit test module for the utils module functions.'''

import unittest
from unittest.mock import patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Test suite for the access_nested_map function.'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Check that access_nested_map returns the correct result.'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''Check that access_nested_map raises a KeyError for invalid paths.'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(context.exception))


class TestGetJson(unittest.TestCase):
    '''Test suite for the get_json function.'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_payload):
        '''Check that get_json returns the expected JSON response.'''
        mock_response = {'return_value.json.return_value': expected_payload}
        with patch('requests.get', **mock_response) as mock_get:
            self.assertEqual(get_json(url), expected_payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    '''Test suite for the memoize decorator.'''

    def test_memoize(self):
        '''Verify that memoize caches the result of a method call.'''

        class TestClass:
            '''A class with a method to be memoized.'''

            def a_method(self):
                """A method to be memoized."""
                return 42

            @memoize
            def a_property(self):
                """A property to be memoized."""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()
