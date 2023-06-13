#!/usr/bin/python3
"""
Contains function that adds and saves to Python obj to JSON file; loads objects
"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    filename = 'add_item.json'

    try:
        file = load_from_json_file(filename)
    except FileNotFoundError:
        file = []
    file.extend(sys.argv[1:])
    save_to_json_file(file, filename)
