#!/usr/bin/python3

"""This module contains a subclass checker function."""


def inherits_from(obj, a_class):

    """Checks if obj is an instance of a class inherited from 
    a_class."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        False
