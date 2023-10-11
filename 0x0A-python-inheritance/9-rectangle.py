#!/usr/bin/python3

"""This module contains the subclass Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class defines a rectangle."""

    def __init__(self, width, height):
        """Instantiates a new rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): height of the rectangle.
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of a
        rectangle description."""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
