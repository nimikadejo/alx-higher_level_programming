#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except Exception:
        pass
        result = None
    finally:
        print("Inside result: {:d}".format(result))
    return result
