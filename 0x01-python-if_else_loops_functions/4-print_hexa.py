#!/usr/bin/python3
"""prints all numbers from 0 to 98 in decimal and hexadecimal forms"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
