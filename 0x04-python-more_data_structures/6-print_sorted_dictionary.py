#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = items(sorted(a_dictionary))
    for k, v in new_dict:
        print("{:s}: {}".format(k, v))
