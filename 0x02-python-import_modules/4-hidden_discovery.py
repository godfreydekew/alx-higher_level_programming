#!/usr/bin/python3.8
if __name__ == '__main__':
    import hidden_4

    my_list = dir(hidden_4)

    for i in range(len(my_list)):
        name = my_list[i]
        if name[:2] != "__":
            print(name)
