#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = "arguments:"
    if len(sys.argv) == 2:
        args = "argument:"
    if len(sys.argv) == 1:
        args = "arguments."

    print("{:d} {:s}".format(len(sys.argv) - 1, args))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
