#!/usr/bin/python3
"""
Module contains class Rectangle
Inherits from Base;
"""


from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        if not isinstance(value, int):
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be greater than zero")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an intger")
        if value < 0:
            raise ValueError("height must be greater than zero")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        if not isinstance(value, int):
            raise TypeError("x must be an intger")
        if value < 0:
            raise ValueError("x must be greater than zero")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if not isinstance(value, int):
            raise TypeError("y must be an intger")
        if value < 0:
            raise ValueError("y must be greater than zero")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print to stdout a rectangle using #'s"""
        print("\n" * self.y +
                "\n".join((" " * self.x + "#" * self.width)
                          for i in range(self.height)))

    def __str__(self):
        """print the rectangle info"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update thd rectangle attr"""
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]