#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in list(a_dictionary):
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
