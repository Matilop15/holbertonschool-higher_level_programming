#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
8-rectangle.py
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
add width and heigth
"""


class BaseGeometry:
    """
    add integer validator to anterior task
    """
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

    class Rectangle(BaseGeometry):
        """create subclass Rectanble of BaseGeometry"""

        def __init__(self, width, height):
            """
            width and height must be privat
            and must be positive integer
            """
            self.__width = width
            self.__height = height

            self.integer_validator("width", width)
            self.integer_validator("height", height)
