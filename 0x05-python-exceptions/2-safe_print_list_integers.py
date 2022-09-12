#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_len = 0

    for item in range(x):
        try:
            print("{:d}".format(my_list[item], end=""))
            int_len += 1
        except IndexError as Err:
            print("{}: list index out of range".format(Err.args))
        except Exception:
            pass
    print('')
    return int_len
