#!/usr/bin/python3
"""prints the alphabet in lowercase without adding a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)),end="")
