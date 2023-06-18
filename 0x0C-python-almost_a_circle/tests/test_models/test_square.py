#!/usr/bin/python3
"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class created is indeed Rectangle"""
    def test_square_class(self):
        """test square class"""
        self.assertEqual(type(Square(3)), Square)
        self.assertTrue(isinstance(Square(3), Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))


    def test_all_atrr(self):
        """Test all attributes match what's given"""
        r = Square(3, 2, 2, 100)
        self.assertTrue(r.size == 3)
        self.assertTrue(r.x == 2)
        self.assertTrue(r.y == 2)
        self.assertTrue(r.id == 100)

    def test_def_attr(self):
        """Test default attributes are set when not given"""
        r = Square(3)
        self.assertTrue(r.size == 3)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)
        self.assertTrue(r.id is not None)

    def test_private_attr(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Square.__size)
            print(Square.__x)
            print(Square.__y)

    def test_attr_validate(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an intger"):
            Square("2")
            Square([1])    
        with self.assertRaisesRegex(TypeError, "x must be an intger"):
            Square(3, None)
            Square(3, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an intger"):
            Square(3, 5, (2, 2))
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            Square(-3, 2, 2, 100)
        with self.assertRaisesRegex(ValueError, "x must be greater than zero"):
            Square(3, -2, 2, 100)
        with self.assertRaisesRegex(ValueError, "y must be greater than zero"):
            Square(3, 2, -2, 100)

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_str(self):
        """test print the square attrs"""
        self.assertEqual(str(Square(4, 2, 1, 12)), "[Square] (12) 2/1 - 4")
        self.assertEqual(str(Square(5, 1, 0, 1)), "[Square] (1) 1/0 - 5")

    def test_update(self):
        """test update attr func by args & kwargs"""
        r = Square(10, 10, 10, 10)
        self.assertEqual(str(r), '[Square] (10) 10/10 - 10')
        r.update()
        self.assertEqual(str(r), '[Square] (10) 10/10 - 10')
        r.update(5)
        self.assertEqual(str(r), '[Square] (5) 10/10 - 10')
        r.update(5, 4)
        self.assertEqual(str(r), '[Square] (5) 10/10 - 4')
        r.update(5, 4, 3)
        self.assertEqual(str(r), '[Square] (5) 3/10 - 4')
        r.update(5, 4, 3, 2)
        self.assertEqual(str(r), '[Square] (5) 3/2 - 4')
        r.update(id = 10)
        self.assertEqual(str(r), '[Square] (10) 3/2 - 4')
        r.update(id = 10, size = 10)
        self.assertEqual(str(r), '[Square] (10) 3/2 - 10')
        r.update(id = 10, size = 10, x = 10)
        self.assertEqual(str(r), '[Square] (10) 10/2 - 10')
        r.update(id = 10, size = 10, x = 10, y = 10)
        self.assertEqual(str(r), '[Square] (10) 10/10 - 10')
        with self.assertRaisesRegex(TypeError, "width must be an intger"):
            r.update(10, "10", 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            r.update(10, -10, 10, 10)
        r.update(no_id = 10, n_size = 10, x = 5, y = 4)
        self.assertEqual(str(r), '[Square] (10) 5/4 - 10')

    def test_to_dictionary(self):
        """test to_dictionary method"""
        s1 = Square(10, 1, 9).to_dictionary()
        self.assertTrue(isinstance(s1, dict))