#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = items(sorted(a_dictionary))
    print("{:s}: {}".format(new_dict.keys, new_dict.value))
