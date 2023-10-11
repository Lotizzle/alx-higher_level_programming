#!/usr/bin/python3
"""Defines a subclass MyInt that inherits from int."""


class MyInt(int):
    """This class inverts int operators == and !=."""

    def __eq__(self, value):
        """switches == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """switches != operator with == behavior."""
        return self.real == value
