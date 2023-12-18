#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    result = 0
    for i in range(list_length):

        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            my_list.append(result)

    return my_list
