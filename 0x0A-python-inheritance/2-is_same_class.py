#!/usr/bin/python3

""" This module defines a object type check function."""


def is_same_class(obj, a_class):

    """This function returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
