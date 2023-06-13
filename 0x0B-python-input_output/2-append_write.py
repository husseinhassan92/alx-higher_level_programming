#!/usr/bin/python3
"""
Contains function that apeends to text file and returns num chars written
"""


def append_write(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, 'a') as f:
        return f.write(text)
