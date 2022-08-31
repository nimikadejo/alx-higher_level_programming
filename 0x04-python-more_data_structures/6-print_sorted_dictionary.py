#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary)
    for item in new_dict:
        print("{}: {}".format(item, new_dict[item]))
