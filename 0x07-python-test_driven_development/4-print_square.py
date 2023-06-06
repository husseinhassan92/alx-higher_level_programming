#!/usr/bin/python3
"""
Module 4-print_square
Contains method that prints square with #'s
Takes in an int size
"""


def print_square(size):
    """ Prints square with #'s given int size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print("\n".join([("#" * size) for i in range(size)]))
