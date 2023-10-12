#!/usr/bin/python3
"""This module defines a Python class-to-JSON function."""


def class_to_json(obj):
    """This fucntion returns the dictionary represntation
    of a simple data structure."""

    return obj.__dict__
