#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = []
    for k, v in a_dictionary.items():
        times2 = list(map(lambda v: v*2, a_dictionary))
        new_dict.append(times2)
    return {a_dictionary.key: new_dict.value}
