#!/usr/bin/env python3

""" 
    Unit tests for utils.py
"""

import unittest
from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    @parameterized.expand([
        ({"person": {"bio": {"name": "John", "age": 30}}}, ("person", "bio", "name"), "John"),
        ({"person": {"bio": {"name": "John", "age": 30}}}, ("person", "bio", "age"), 30),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"person": {"bio": {"name": "John", "age": 30}}}, ("person", "bio", "address"), "address"),
        ({"person": {"bio": {"name": "John", "age": 30}}}, ("person", "address"), "address"),
    ])
    def test_access_nested_map_with_key_error(self, nested_map, path, expected):
        """Test access_nested_map with KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))
