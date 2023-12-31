#!/usr/bin/python3

"""This module contains only one function (lookup)."""


def lookup(obj):
    """The lookup function returns a list of the attributes
    and methods of an object.

    Arg:
        obj (any): Variable for object type.
    """

    return (dir(obj))
