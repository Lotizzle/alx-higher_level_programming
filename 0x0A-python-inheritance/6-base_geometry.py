#!/usr/bin/python3

""" This module defines a class that raises an exception."""


class BaseGeometry:
    """This class performs basic geometry."""

    def area(self):
        """This function raises an exception with a message."""

        raise Exception("area() is not implemented")
