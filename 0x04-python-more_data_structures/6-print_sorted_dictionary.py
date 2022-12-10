#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dicKey = list(a_dictionary.keys())
    dicKey.sort()
    for item in dicKey:
        print("{}: {}".format(item, a_dictionary.get(item)))
