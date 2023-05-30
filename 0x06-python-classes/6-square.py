#!/usr/bin/python3
"""creating square class
"""


class Square:
    """class for square properties"""
    def __init__(self, size=0, position=(0, 0)):
        """initiating square class"""
        self.size = size
        self.position = position

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
        """"
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter
        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if (type(value) is not tuple or len(value) != 2 or
           type(value[0]) is not int or type(value[1]) is not int or
           value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
