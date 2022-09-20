#!/usr/bin/python3
"""
    This module prints a square
    with function print_square
"""


def print_square(size):
    """
    prints a square as "#" based on size

    Args:
        size(int)
    """

    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
