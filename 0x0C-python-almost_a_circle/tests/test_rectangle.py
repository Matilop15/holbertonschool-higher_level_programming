#!/usr/bin/python3
"""
Test for rectangle.py
"""

import unittest

from models.base import Base

from models.rectangle import Rectangle

class test_case(unittest.TestCase):
    """Test for rectangle.py"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """check if call id"""
        res = Rectangle(10, 2)
        self.assertEqual(res.id, 1)

    def test_id2(self):
        """check multipl call di"""
        res = Rectangle(10, 2)
        res2 = Rectangle(2, 4, 0, 0, 12)
        res3 = Rectangle(2, 4)
        self.assertEqual(res3.id, 2)

    def test_complete(self):
        """ check for attributes values"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_errors(self):
        """check differents errors"""
        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
                "__init__() missing 1 required positional argument: 'height'", str(
                    x.exception))
        _str = ("__init__() missing 2 required positional" +
                " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(_str, str(x.exception))

    def test_inheritance(self):
        """check for inheritance"""
        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_attributes(self):
        """check for atributes"""
        with self.assertRaises(TypeError) as x:
            Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle(1, 2, "Holbie", 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle(1, 2, 2, "Matias")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))

    def test_area(self):
        """Check area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(75, 2)
        self.assertEqual(r2.area(), 150)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
                "area() takes 1 positional argument but 2 were given", str(
                    x.exception))
