#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
import pep8

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger


        Args:
        unittest ([list]): list of integers
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['6-max_integer.py'])
        self.assertEqual(result.total_errors, 0, "Found" +
                         " code style errors (and warnings).")

    def test_checkType(self):
        """Test to check the most common example"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        """Test to check if the list is empty"""
        self.assertEqual(max_integer([]), None)
