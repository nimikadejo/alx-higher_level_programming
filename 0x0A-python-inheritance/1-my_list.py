#!/usr/bin/python3
"""
A class that inherits from list
"""


class MyList(list):
    """ my_list inheriting from list"""
def print_sorted(self):
    """prints sorted list in ascesding order
    """
    print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
