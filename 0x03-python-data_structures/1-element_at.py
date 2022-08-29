#!/usr/bin/python3
def element_at(my_list, idx):
    if (not isinstance(idx, int)):
        return None
    elif idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
#    elif (len(mylist)) == 0:
#        return None
    return my_list[idx]
