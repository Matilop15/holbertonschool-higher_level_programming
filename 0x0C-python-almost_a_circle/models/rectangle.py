#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
Write the class Rectangle that inherits from Base
"""


class Rectangle(Base):
    """ subclase de Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """lados del rectangulo"""
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y




