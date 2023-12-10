#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    my_dict = {}
    for k, v in a_dictionary.items():
        my_dict[k] = v * 2
    return my_dict
