#!/usr/bin/python3
def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value"""
    if a_dictionary is not None:
        my_max = max(a_dictionary.values())
        for k, v in a_dictionary.items():
            if v == my_max:
                return k
    else:
        return 'None'
