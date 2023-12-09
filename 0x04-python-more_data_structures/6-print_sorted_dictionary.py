#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dict = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for key, value in my_dict.items():
        print("{:s}: {:s}".format(str(key), str(value)))
