#!/usr/bin/python3
"""
Contains method is_kind_of_class
returns True if object is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use isinstance() to get class and any parent classes too
    Return:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
