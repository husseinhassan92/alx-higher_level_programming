#!/usr/bin/python3
"""
Contains function that adds and saves to Python obj to JSON file; loads objects
"""


import sys

if __name__ == "__main__":
    from (5-save_to_json_file) import save_to_json_file
    from (6-load_from_json_file) import load_from_json_file

    filename = 'add_item.json'

    try:
        file = load_from_json_file(filename)
    except FileNotFoundError:
        file = []
    file.extend(sys.argv[1:])
    save_to_json_file(file, filename)
