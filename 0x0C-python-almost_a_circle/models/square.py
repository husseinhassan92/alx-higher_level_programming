#!/usr/bin/python3
"""
Module contains class Suare
Inherits from Base;
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Rectangle; inherits from class Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize rectangle class"""
        super().__init__( size, size, x, y, id)

    