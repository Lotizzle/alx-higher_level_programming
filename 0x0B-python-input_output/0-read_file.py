#!/usr/bin/python3

"""This module defines a text file reading function."""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The default file name is an empty string.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
