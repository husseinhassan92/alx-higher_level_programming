#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for models/base.py"""
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

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
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)
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
                             json.dumps([r1.to_dictionary(),
                                         r2.to_dictionary()]))

            Rectangle.save_to_file(None)
            with open("Rectangle.json", "r") as file:
                self.assertEqual('[]', file.read())

            Rectangle.save_to_file([])
            with open("Rectangle.json", "r") as file:
                self.assertEqual('[]', file.read())

    def test_from_json_string(self):
        """test from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4},
                                       {'id': 7, 'width': 1, 'height': 7}])

        list_input_1 = None
        json_list_input = Rectangle.to_json_string(list_input_1)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))
        self.assertEqual(list_output, [])

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))
        self.assertEqual(list_output, [])

    def test_create(self):
        """test create method"""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
