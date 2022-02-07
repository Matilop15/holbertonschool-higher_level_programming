#!/usr/bin/python3
"""
Test for base.py
"""

import unittest

from models.base import Base


class test_case(unittest.TestCase):
    """holberton"""
    def setUp(self):
        Base._Base__nb_objects = 0
    
    def test_base(self):
        """
        check if base id no args
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_baseNone(self):
        """
        check if base id is None
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)

    def test_base_12(self):
        """
        check if base id with 1 arg
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_inc(self):
        """
        check if base id increment
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_id_inc2(self):
        """
        check if base id increment
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_id_neg(self):
        """
        check base id negaative
        """
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_id_str(self):
        """
        check base id str
        """
        b1 = Base('hola')
        self.assertEqual(b1.id, 'hola')

    def test_id_float(self):
        """
        check base id float
        """
        b1 = Base(1.0)
        self.assertEqual(b1.id, 1.0)

    def test_id_bool(self):
        """
        check base id bool
        """
        b1 = Base(True)
        self.assertEqual(b1.id, True)
