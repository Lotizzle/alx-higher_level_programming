#!/usr/bin/python3

"""This module defines a text appending function."""


def append_write(filename="", text=""):
    """This function appends a string of text at the end of a file.

    Args:
        filename: The file.
	text: The string to append.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
