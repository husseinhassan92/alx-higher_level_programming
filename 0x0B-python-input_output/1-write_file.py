#!/usr/bin/python3
"""
Contains function that writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, 'w') as f:
        return f.write(text)
