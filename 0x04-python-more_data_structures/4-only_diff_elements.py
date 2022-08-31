#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = []
    for ele in set_1 ^ set_2:
        diff_elements.append(ele)
    return (diff_elements)
