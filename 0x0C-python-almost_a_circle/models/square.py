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

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """print the square info"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size)

    def update(self, *args, **kwargs):
        """ update thd square attr"""
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ return dict of attrs"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
    