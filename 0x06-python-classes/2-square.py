#!/usr/bin/python3

""" This is a file to creat a Class called Square and
its possible methods, objects or attributes
"""


class Square:

    """ Square class:

    This is a class Square that defines a square.
    It contains a private instance attribute, size and the __init__ method.
    """

    def __init__(self, size=0):

        """ Initializes the data.

        Args:
            size (int): the size of the square.

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
