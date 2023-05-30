#!/usr/bin/python3
"""creating square class
"""


class Square:
    """class for square properties"""
    def __init__(self, size=0):
        """initiating square class"""
        self.__size = size

    @property
    def size(self):
        """
        return size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setting the size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate area of square
        Returns:
            area
        """
        return self.__size * self.__size
