#!/usr/bin/python3

""" This creates a class called a Rectangle that defines a rectangle. """


class Rectangle:

    """ This class contains some private instance attributes and  methods """
    def __init__(self, width=0, height=0):

        """ Initializes the data.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

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
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ Returns the area of Rectangle

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        """

        return self.__width * self.__height

    def perimeter(self):

        """ Returns the perimeter of Rectangle using the class attributes
            
            Attributes:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.

        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
