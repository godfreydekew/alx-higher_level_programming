#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):

                print("{:d}".format(my_list[i]), end="")
                no += 1
        print()
        return no
    except (TypeError, ValueError):
        return no
