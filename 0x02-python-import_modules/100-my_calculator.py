#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, div, mul, sub

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        args = sys.argv
        a = int(args[1])
        op = args[2]
        b = int(args[3])

        result = None
        if (op == "+"):
            result = add(a, b)
        elif (op == "-"):
            result = sub(a, b)
        elif (op == '*'):
            result = mul(a, b)
        elif (op == "/"):
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}" .format(a, op, b, result))
        sys.exit(0)
