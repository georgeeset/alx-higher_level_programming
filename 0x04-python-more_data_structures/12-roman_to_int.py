#!/usr/bin/python3

def roman_to_int(roman_string):
    figures = {"I": 1, "V": 5, "X": 10,
               "L": 50, "C": 100, "D": 500, "M": 1000}
    num = []
    store = 0

    if not type(roman_string) == str:
        return (0)

    if not roman_string:
        return (0)

    for char in roman_string:
        num.append(figures[char])
        length = len(num)
        if length > 1:
            if num[length-1] > num[length-2]:
                num[length - 1] = num[length - 1] - num[length - 2]
                num[length - 2] = 0

    for item in num:
        store += item
    return (store)
