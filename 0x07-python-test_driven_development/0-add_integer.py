#!/usr/bin/python3
"""
    add_integer: adds two integers
"""


def add_integer(a, b):
    """ returns the sum of two numbers, a and b
    Args:
    a (int) : first parameter
    b (int) :  second parameter
    """

    if a != a or b != b:
        return float('nan')
    if a == float('inf') or a == -float('inf'):
        return float('inf')
    if b == float('inf') or b == -float('inf'):
        return float('inf')
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
