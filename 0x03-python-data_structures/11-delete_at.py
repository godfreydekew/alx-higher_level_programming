#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    
    if idx in range(len(my_list)):
        return [i for i in my_list if my_list.index(i) != idx]
    return my_list
