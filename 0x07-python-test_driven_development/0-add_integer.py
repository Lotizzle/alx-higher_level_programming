#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ This function perfoms the integer addition of a and b.

    Returns the integer addition of two numbers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
