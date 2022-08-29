#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = mylist[:]
    if (not isinstance(idx, int)):
        return my_list.copy()
    if idx < 0:
        return my_list.copy()
    if idx > len((my_list) - 1):
        return my_list.copy()
    new_list[idx] = element
    return new_list
