#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argsCount = len(sys.argv) - 1
    value = 0

    if argsCount > 0:
        for item in sys.argv:
            if item == sys.argv[0]:
                continue
            value += int(item)
    print(value)
