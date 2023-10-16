#!/usr/bin/python3
"""This module contains the base class which is our first class."""


class Base:
    """
    Base class to manage id attribute in all future classes
    and to avoid duplicating the same code
    (by extension, same bugs).
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
