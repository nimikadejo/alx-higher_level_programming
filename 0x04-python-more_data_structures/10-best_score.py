#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    the_name = ''
#    if a_dictionary is None:
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary[key]
            the_name = key
    return (the_name)
