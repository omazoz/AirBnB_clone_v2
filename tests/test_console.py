#!/usr/bin/python3
""" Module doc"""
import unittest
import console


class test_Console(unittest.TestCase):
    """test console"""

    def test_documentation(self):
        """test console"""
        self.assertIsNotNone(console.__doc__)
