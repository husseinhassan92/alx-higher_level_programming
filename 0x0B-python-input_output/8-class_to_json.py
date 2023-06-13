#!/usr/bin/python3
"""
Contains function that
returns dictionary description with simple data structure
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
       (list, dictionary, dictionary, string)
       for JSON serialization of an object
    Args:
        obj: python object
    """
    return obj.__dict__
