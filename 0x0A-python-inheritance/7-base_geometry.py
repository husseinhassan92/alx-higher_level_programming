#!/usr/bin/python3
"""
Contains BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input
        Args:
            name (str): assumed always a string
            value (int): greater than 0
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))