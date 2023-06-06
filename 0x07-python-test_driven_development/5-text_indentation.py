#!/usr/bin/python3
"""
Module 5-text_indentation
Contains method that prints text with 2 new lines after each ".", "?", and ":"
Takes in a string
"""


def text_indentation(text):
    """ Prints text with 2 new lines after each ".", "?", and ":" """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i] + "\n\n", end="")
            i += 1
        elif text[i] in ".?:" and text[i+1] == " ":
            i += 1
        else:
            print(text[i], end="")
        i += 1
