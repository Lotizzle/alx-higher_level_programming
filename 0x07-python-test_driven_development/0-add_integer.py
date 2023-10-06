#!/usr/bin/python3
"""Defines an integer addition function.
This function perfoms the addition of a and b.

Raises:
    TypeError: if either a or b isn't a type int or float.
"""


def add_integer(a, b=98):
    """ This function perfoms the addition of a and b.

    Args:
        a: First integer or float
        b: Second integer or float

    Returns a + b
    """

    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
