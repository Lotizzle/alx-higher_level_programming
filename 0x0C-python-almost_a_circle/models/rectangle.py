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

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle.

        Args:
            *args (ints): The new attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): The new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle."""

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Prints the properties of the Rectangle class."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
