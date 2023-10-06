#!/usr/bin/python3
"""Defines a integer addition function."""


def add_integer(a, b=98):
    """ This function perfoms the addition of a and b.
    a and b are first casted to integers if they are floats.

    Raises:
        TypeError: if either a or b isn't a type int or float.
    """

    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a)+int(b))
