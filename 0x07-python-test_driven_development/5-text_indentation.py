#!/usr/bin/python3
"""
module for the function `text_indentation`
which prints a text with 2 new lines after every ". ? :"
"""


def text_indentation(text):
    """adds two lines after  every char of `.`, `:` and `?`
    Args:
        text(str)
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i, '\n' * 2, end="", sep="")
        else:
            print(i, end="", sep="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
