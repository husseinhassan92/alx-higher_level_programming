#!/usr/bin/python3
"""
creating rectangle class
"""


class Rectangle:
    """
    define Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height


@property
def width(self):
    """
    return the width value
    """
    return self.__width


@width.setter
def width(self, value):
    """
    assgin the width value
    """
    if type(value) is not int:
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = value


@property
def height(self):
    """
    return the height value
    """
    return self.__height


@height.setter
def height(self, value):
    """
    assgin the height value
    """
    if type(value) is not int:
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.self.__height = value
