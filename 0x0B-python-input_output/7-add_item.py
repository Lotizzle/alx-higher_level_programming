#!/usr/bin/python3
""" This module contains a script that adds all arguments
to a Python list, and then saves them to a file."""
import sys


saveJSON = __import__('5-save_to_json_file').save_to_json_file
loadJSON = __import__('6-load_from_json_file').load_from_json_file

try:
    loadfile = loadJSON('add_item.json')
except Exception:
    loadfile = []

loadfile += sys.argv[1:]

saveJSON(loadfile, 'add_item.json')
