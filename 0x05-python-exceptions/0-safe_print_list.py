#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
            length += 1
        except Exception as Err:
            break
    print('')
    return length
