#!/usr/bin/python3

if __name__ == "__main__":
    """Import the module add_0 and use function add"""
    import add_0
    add = add_0.add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
