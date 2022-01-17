#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        return None
    finally:
        if res == 0:
            res = None
            print("Inside result: {}".format(res))
            return None
        else:
            print("Inside result: {}".format(res))
            return res
