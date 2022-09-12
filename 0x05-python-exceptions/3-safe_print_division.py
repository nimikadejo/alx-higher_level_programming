def safe_print_division(a, b):
    try:
        result = a / b
    finally:
        print("Inside result: {:d}".format(result))
    except Exception:
        result = None
    return result
