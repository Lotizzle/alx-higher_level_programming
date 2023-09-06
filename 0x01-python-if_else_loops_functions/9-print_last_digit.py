#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number"""
    digit = abs(number) % 10
    print(digit, end="")
    return (digit)
