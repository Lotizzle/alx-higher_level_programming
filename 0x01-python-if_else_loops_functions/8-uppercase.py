#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase 
    followed by a new line"""
    result_str = ""

    for char in str:
        if 'a' <= char <= 'z':
            result_str += chr(ord(char) - 32)
        else:
            result_str += char

    print("{}".format(result_str), end="")
    print("{}".format(""))
