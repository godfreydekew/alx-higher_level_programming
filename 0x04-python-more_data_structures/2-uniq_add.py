#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    return sum(unique_list)
