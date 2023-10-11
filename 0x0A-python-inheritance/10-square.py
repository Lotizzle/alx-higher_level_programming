#!/usr/bin/python3
"""Defines the subclass Square of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
