#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for m in my_list:
        new_list.append(m if m != search else replace)
    return (new_list)
