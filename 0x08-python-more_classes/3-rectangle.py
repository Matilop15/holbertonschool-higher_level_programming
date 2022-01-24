#!/usr/bin/python3
"""
3-rectangle
a class Rectangle that defines a rectangle by: (based on 2-rectangle)
print a rectagle with #
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """calculate area and perimeter of rectangle
        and print a rectangle with #
        """
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
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        ''' return area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter of rectangle '''
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        '''return a rectangle'''
        rect = ""
        if 0 in [self.__width, self.__height]:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i != self.__height - 1:
                rect += "\n"
        return rect
