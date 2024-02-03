#!/usr/bin/python3

def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value"""
    if a_dictionary is not None:
        my_max = max(a_dictionary.values())
        k = [i for i in a_dictionary if a_dictionary[i] == my_max]
        return k[0]
    else:
        return 'None'
