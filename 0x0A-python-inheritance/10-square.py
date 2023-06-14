#!/usr/bin/python3
"""
Contains parent class Rectangle
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """inherits from Rectangle
    Methods:
        def __init__(self, size):
    """
    def __init__(self, size):
        """validate and initialize size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
