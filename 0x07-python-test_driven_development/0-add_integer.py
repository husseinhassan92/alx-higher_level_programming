#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that returns an int sum
Accepts two values, whether int or float, and casts them to int before adding
"""


def add_integer(a, b=98):
    """ Return a + b as int"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an intege")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an intege")
    return int(a) + int(b)
