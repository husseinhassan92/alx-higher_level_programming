#!/usr/bin/python3
"""creating square class
"""


class Square:
    """class for square properties"""
    def __init__(self, size=0):
        """initiating square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculate area of square
        Returns:
            area
        """
        return self.__size * self.__size
