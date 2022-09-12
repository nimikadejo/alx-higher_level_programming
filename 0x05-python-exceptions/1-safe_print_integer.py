#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new_value = isinstance(int(value))

    except Exception as error:
        print("{} is not an integer".format(value))
        return False
    else:
        print("{:d}".format(value))
        return True
