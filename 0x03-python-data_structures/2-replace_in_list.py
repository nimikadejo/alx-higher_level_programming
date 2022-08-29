#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (not isinstance(idx, int)):
        return 0
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    elif (len(my_list)) == 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
