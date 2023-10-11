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

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
