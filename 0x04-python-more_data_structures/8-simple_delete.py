#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    key_set = set(a_dictionary.keys())
    if key in key_set:
        a_dictionary.pop(key)
    return (a_dictionary)
