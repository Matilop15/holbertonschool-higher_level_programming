#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
Test for square.py
"""


from models.base import Base

from models.rectangle import Rectangle

from models.square import Square

import unittest

import pycodestyle


class TestSquare(unittest.TestCase):
    """test for square"""

    def test_pep8_scuare(self):
        """
        Test that checks PEP8 in square
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in square.py"
        )

    def test_pep8_test_scuare(self):
        """
        Test that checks PEP8 in test_square
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_square.py"
        )
