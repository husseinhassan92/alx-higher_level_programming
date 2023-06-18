#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase(unittest.TestCase):
    """Tests for models/base.py"""

    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(10), self.id == 10)
        self.assertTrue(Base(99), self.id == 99)
        self.assertTrue(Base(1000), self.id == 1000)

    def test_id_not_given(self):
        """Test ids match when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_private_attr(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_to_json_string(self):
        """ test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(json_dictionary, str))
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        d2 = None
        strd2 = Base.to_json_string([d2])
        self.assertTrue(isinstance(strd2, str))
        self.assertTrue(strd2, "[]")
        d3 = {}
        strd3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(isinstance(strd3, str))
        self.assertTrue(strd3, "[]")


    def test_save_to_file(self):
        """ test save to file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),
                             json.dumps([r1.to_dictionary(), r2.to_dictionary()]))
            
            Rectangle.save_to_file(None)
            with open("Rectangle.json", "r") as file:
                self.assertEqual('[]', file.read())
            
            Rectangle.save_to_file([])
            with open("Rectangle.json", "r") as file:
                self.assertEqual('[]', file.read())
