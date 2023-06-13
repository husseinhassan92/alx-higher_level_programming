#!/usr/bin/python3
"""
Contains function that reads and prints contents from file
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename) as f:
        print(f.read(), end="")
