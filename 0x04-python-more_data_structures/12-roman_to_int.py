#!/usr/bin/python3

def roman_to_int(roman_string):
    figures = {"I":1,"IV":4, "V":5, "IX": 9, "X": 10,
                     "XL": 40, "L": 50, "XC": 90, "C": 100,
                     "CD": 400, "D": 500, "CM": 900, "M": 1000}
    num = []
    store = 0

    if not roman_string:
        return (0)
    if not str(roman_string):
        return (0)

    for char in roman_string:
        num.append(figures[char])
        length = len(num)
        if length > 1:
            if num[length-1] > num[length-2]:
                num[length -1] = num[length - 1] - num[length -2]
                num[length -2] = 0

    for item in num:
        store += item
    return (store)
