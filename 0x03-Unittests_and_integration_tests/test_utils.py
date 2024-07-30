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
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"a": {"b": {"c": 1}}}, ["a", "b", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["a", "c", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["b", "c", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c", "d"], None),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"a": {"b": {"c": 1}}}, ["a", "b", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["a", "c", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["b", "c", "d"], None),
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c", "d"], None),
    ])
    def test_access_nested_map_with_key_error(self, nested_map, path, expected):
        """Test access_nested_map with KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))
