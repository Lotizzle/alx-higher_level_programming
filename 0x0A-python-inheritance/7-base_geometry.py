#!/usr/bin/python3

""" This module defines a class that raises an exception."""


class BaseGeometry:
    """This class performs basic geometry."""

    def area(self):
        """This function raises an exception with a message."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """This function validates a value given."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
