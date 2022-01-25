#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCases for the max_integer function"""

    def test_int(self):
        """Test with list if int, return the max result"""
        _list = [1, 2, 3, 4, 5]
        res = max_integer(_list)
        self.assertEqual(res, 5)

    def test_float(self):
        """Test with list of float, return max float"""
        _list = [4.3, 4.11, 3.1]
        res = max_integer(_list)
        self.assertEqual(res, 4.3)
    def test_empty(self):
        """Test with empty list"""
        _list = []
        res = max_integer(_list)
        self.assertEqual(res, None)

    def test_negative(self):
        """Test with all int are negatives"""
        _list = [-12, -123, -1]
        res = max_integer(_list)
        self.assertEqual(res, -1)

    def test_float_negative(self):
        """Test whith all float negatives"""
        _list = [-2.3, -4.5 , -3.3]
        res = max_integer(_list)
        self.assertEqual(res, -2.3)

    def test_string(self):
        """Test with list of string"""
        _list = ["hello", "school"]
        res = max_integer(_list)
        self.assertEqual(res, "school")


    """The follow test are with ASSERTRAISES"""
    
    def test_int_and_str(self):
        """Test with int and strings, return TypeError"""
        _list = [9, "Hello", 4, "bye"]
        self.assertRaises(TypeError, max_integer, _list)

    def test_str(self):
        """Test error str"""
        _list = ["hola", "hello"]
        res = max_integer(_list)
        self.assertRaises(TypeError, res)

    def test_list_of_list(self):
        """Test list of list"""
        _list = [[9, 6],[3, 5]]
        res = max_integer(_list)
        self.assertRaises(TypeError, res)

    def test_None(self):
        """_list None"""
        self.assertRaises(TypeError)

    def test_true(self):
        """Test with true"""
        _list = [True]
        res = max_integer(_list)
        self.assertRaises(TypeError, res)

    def test_false(self):
        _list = [False]
        res = max_integer(_list)
        self.assertRaises(TypeError, res)

if __name__ == '__main__':
        unittest.main()
