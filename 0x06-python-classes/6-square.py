#!/usr/bin/python3
"""creating square class
"""


class Square:
    """class for square properties"""
    def __init__(self, size=0, position=(0, 0)):
        """initiating square class"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        return position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setting the position of square
        """
        if (not isinstance(value, tuple) or len(value) == 2
           or not isinstance(value[0], int) or
           not isinstance(value[1], int) or
           value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        calculate area of square
        Returns:
            area
        """
        return self.__size * self.__size

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
                print("")
