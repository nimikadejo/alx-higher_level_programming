#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = []
    for ele in set_1 & set_2:
        common_set.append(ele)
    return (common_set)
