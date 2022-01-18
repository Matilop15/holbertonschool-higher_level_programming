#!/usr/bin/python3

class Square:
    """Square Class
    """

    def __init__(self, size=0):
        """
        The __init__ method initializes the size value of the square.
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
     """

        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):

        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns square area
        """
        return self.__size * self.__size
