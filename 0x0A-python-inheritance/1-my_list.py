#!/usr/bin/python3

"""This module contains a subclass called (MyList) and
a method called ``def print_sorted(self)``."""


class MyList(list):
    """ This class is a subclass of the built-in list class."""


    def print_sorted(self):

        """This method returns a sorted list in ascending order."""

        sorted_list = sorted(self)
        print(sorted_list)
