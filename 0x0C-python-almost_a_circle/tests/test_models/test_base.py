#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base



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
