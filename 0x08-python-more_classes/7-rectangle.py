#!/usr/bin/python3
"""
7-rectangle
Print the message Bye rectangle...  when an instance of Rectangle is deleted
Public class attribute print_symbol: Initialized to #.
"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Return number of instances
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        '''Returns the representation the Rectangle'''
        w = str(eval("self.width"))
        h = str(eval("self.height"))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        '''if is del print a mensaje and resta una instancia '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
