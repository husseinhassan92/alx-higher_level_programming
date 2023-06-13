#!/usr/bin/python3
"""
Create class Student
"""


class Student:
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        for JSON serialization of an object
        """
        if attrs == None:
            return self.__dict__
        else:
            attr = {}
            for k in attrs:
                if k in self.__dict__.keys():
                    attr[k] = self.__dict__[k]
            return attr
