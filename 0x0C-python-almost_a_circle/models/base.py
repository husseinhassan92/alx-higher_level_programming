#!/usr/bin/python3
"""
Module contains class Base
"""


import json
import csv


class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)   from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)        save_to_file_csv(cls, list_objs)
        load_from_file(cls)                 load_from_file_csv(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ sve json to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = []
                for obj in list_objs:
                    objs.append(obj.to_dictionary())
                f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """ load json string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance  from dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """crete list of instances"""
        filename = cls.__name__ + ".json"
        try:
            list = []
            with open(filename, "r") as f:
                objs = cls.from_json_string(f.read())
                for obj in objs:
                    list.append(cls.create(**obj))
            return list
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
