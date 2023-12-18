#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
