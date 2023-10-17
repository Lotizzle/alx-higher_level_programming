#!/usr/bin/python3
"""This module defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a rectangle.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
            x(int): The x coordinate of the rectangle.
            y(int): The y coordinate of the rectangle.
            id(int): The identity of the rectangle.
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        elif type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            super().__init__(id)

    @property
    def width(self):

        """ Retrieves the value of width """

        return self.__width

    @width.setter
    def width(self, value):

        """ Sets the value of the width of the Rectangle class.

        Args:
            value (int): the value assigned to width.

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ Retrieves the value of height """

        return self.__height

    @height.setter
    def height(self, value):

        """ Sets the value of the height of the Rectangle class.

        Args:
            value (int): the value assigned to height.

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x coordinate of the Rectangle class."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x coordinate of the Rectangle class."""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y coordinate of the Rectangle class."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y coordinate of the Rectangle class."""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle class."""

        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character #."""

        if self.width == 0 or self.height == 0:
            return ("")

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Prints the properties of the Rectangle class."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
