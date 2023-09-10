#!/usr/bin/python3

if __name__ == "__main__":
    """Import the module add_0 and use function add"""
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
