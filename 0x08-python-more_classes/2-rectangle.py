#!/usr/bin/python3
"""
2-rectangle
a class Rectangle that defines a rectangle by: (based on 1-rectangle)
"""


class Rectangle:
    '''Rectangle class defined by width and height'''

    def __init__(self, width=0, height=0):
        '''calculate area and perimeter of rectangle'''
        self.height = height
        self.width = width

    @property
    def height(self):
        ''' property of heigh'''
        return self.__height

    @property
    def width(self):
        ''' property of widh'''
        return self.__width

    @height.setter
    def height(self, value):
        ''' height setter '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        ''' return area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter of rectangle '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width + self.__height) * 2)
