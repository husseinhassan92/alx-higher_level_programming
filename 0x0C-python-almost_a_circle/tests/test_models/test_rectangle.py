#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class created is indeed Rectangle"""
    def test_rectangle_class(self):
        """test rectangle class"""
        self.assertEqual(type(Rectangle(3, 4)), Rectangle)
        self.assertTrue(isinstance(Rectangle(3, 4), Base))
        self.assertTrue(issubclass(Rectangle, Base))

    def test_all_atrr(self):
        """Test all attributes match what's given"""
        r = Rectangle(3, 4, 2, 2, 100)
        self.assertTrue(r.width == 3)
        self.assertTrue(r.height == 4)
        self.assertTrue(r.x == 2)
        self.assertTrue(r.y == 2)
        self.assertTrue(r.id == 100)

    def test_def_attr(self):
        """Test default attributes are set when not given"""
        r = Rectangle(3, 4)
        self.assertTrue(r.width == 3)
        self.assertTrue(r.height == 4)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)
        self.assertTrue(r.id is not None)

    def test_private_attr(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_attr_validate(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an intger"):
            Rectangle("2", 4)
            Rectangle([1], 3)
        with self.assertRaisesRegex(TypeError, "height must be an intger"):
            Rectangle(3, {4})
            Rectangle(3, {"h": 4})
        with self.assertRaisesRegex(TypeError, "x must be an intger"):
            Rectangle(3, 4, None)
            Rectangle(3, 4, 5.5)
        with self.assertRaisesRegex(TypeError, "y must be an intger"):
            Rectangle(3, 4, 5, (2, 2))
        with self.assertRaisesRegex(ValueError,
                                    "width must be greater than zero"):
            Rectangle(-3, 4, 2, 2, 100)
        with self.assertRaisesRegex(ValueError,
                                    "height must be greater than zero"):
            Rectangle(3, -4, 2, 2, 100)
        with self.assertRaisesRegex(ValueError, "x must be greater than zero"):
            Rectangle(3, 4, -2, 2, 100)
        with self.assertRaisesRegex(ValueError, "y must be greater than zero"):
            Rectangle(3, 4, 2, -2, 100)

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_area(self):
        """test the area of rectangle method"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(3, 4, 1, 1).area(), 12)
        self.assertEqual(Rectangle(3, 4, 1, 1, 100).area(), 12)
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4)
            r.area(3)
            r.area(3, 4)

    def test_display(self):
        """Test method: display"""
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(5, 3).display()
            b = buf.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(5, 3, 1, 2).display()
            b = buf.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_str(self):
        """test print the rectangle attrs"""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1, 0, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """test update attr func by args & kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(5)
        self.assertEqual(str(r), '[Rectangle] (5) 10/10 - 10/10')
        r.update(5, 4)
        self.assertEqual(str(r), '[Rectangle] (5) 10/10 - 4/10')
        r.update(5, 4, 3)
        self.assertEqual(str(r), '[Rectangle] (5) 10/10 - 4/3')
        r.update(5, 4, 3, 2)
        self.assertEqual(str(r), '[Rectangle] (5) 2/10 - 4/3')
        r.update(5, 4, 3, 2, 1)
        self.assertEqual(str(r), '[Rectangle] (5) 2/1 - 4/3')
        r.update(id=10)
        self.assertEqual(str(r), '[Rectangle] (10) 2/1 - 4/3')
        r.update(id=10, width=10)
        self.assertEqual(str(r), '[Rectangle] (10) 2/1 - 10/3')
        r.update(id=10, width=10, height=10)
        self.assertEqual(str(r), '[Rectangle] (10) 2/1 - 10/10')
        r.update(id=10, width=10, height=10, x=10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/1 - 10/10')
        r.update(id=10, width=10, height=10, x=10, y=10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        with self.assertRaisesRegex(TypeError, "width must be an intger"):
            r.update(10, "10", 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                                    "width must be greater than zero"):
            r.update(10, -10, 10, 10, 10)
        r.update(no_id=10, n_width=10, height=2, x=5, y=4)
        self.assertEqual(str(r), '[Rectangle] (10) 5/4 - 10/2')

    def test_to_dictionary(self):
        """test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9).to_dictionary()
        self.assertTrue(isinstance(r1, dict))
