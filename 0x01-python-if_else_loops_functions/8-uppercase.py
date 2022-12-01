#!/usr/bin/python3
def uppercase(str):
    for cha in str:
        if ord(cha) > 96 and ord(cha) < 123:
            newChar = ord(cha) - 32
        else:
            newChar = ord(cha)
        print("{:c}".format(newChar), end='')
    print()
