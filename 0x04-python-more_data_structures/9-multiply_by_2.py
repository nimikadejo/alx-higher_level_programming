#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = []
    for key, value in a_dictionary.items():
        times2 = list(map(lambda value: value**2, a_dictionary))
        new_dict.append(times2)
        print("{}: {:d}".format(a_dictionary.key, new_dict.value))
    return new_dict
