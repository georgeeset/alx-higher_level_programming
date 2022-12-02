#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, mul, div, sub

    length = len(sys.argv)
    actions = "/*+-"
    usageMsg = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    errMsg = "Unknown operator. Available operators: +, -, * and /"
    a = 0
    b = 0
    result = 0

    if length != 4:
        print(usageMsg)
        sys.exit(1)
    action = sys.argv[2]
    if action not in actions:
        print(errMsg)
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if action == actions[0]:
        result = div(a, b)
    elif action == actions[1]:
        result = mul(a, b)
    elif action == actions[2]:
        result = add(a, b)
    elif action == actions[3]:
        result = sub(a, b)

    print("{} {} {} = {}".format(a, action, b, result))
