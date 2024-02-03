#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for k, val in a_dictionary.items():
            if val == value:
                del a_dictionary[k]
                break
    return a_dictionary
