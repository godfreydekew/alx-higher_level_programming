#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_len = 0
    try:
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
            my_len += 1
        print()
        return int(my_len)

    except IndexError:
        print()
        return int(my_len)
