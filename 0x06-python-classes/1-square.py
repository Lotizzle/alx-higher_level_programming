#!/usr/bin/python3

""" This is a file to creat a Class called Square and
its possible methods, objects or attributes
"""


class Square:

    """ Square class:

    This is a class Square that defines a square.
    It contains a private instance attribute, size and the __init__ method.
    """

    def __init__(self, size):

        """ Initializes the data.

        Args:
            size (int): the size of the square.

        """

        self.__size = size
