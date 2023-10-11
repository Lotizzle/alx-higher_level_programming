#!/usr/bin/python3

"""This module defines a text writing function."""


def write_file(filename="", text=""):

    """This function writes some text to a file.

    Args:
        filename: opened file
        text: string written to filename.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
