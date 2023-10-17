#!/usr/bin/python3
"""This module contains the base class which is our first class."""
import json
import csv


class Base:
    """
    Base class to manage id attribute in all future classes
    and to avoid duplicating the same code
    (by extension, same bugs).
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """This method initializes a new base instance."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
