#!/usr/bin/python3
"""
Contains function that writes Python obj to file using JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename) as f:
        return json.dump(my_obj, f)
