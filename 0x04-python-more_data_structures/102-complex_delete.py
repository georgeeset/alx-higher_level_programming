#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    stage = a_dictionary.copy()
    for index, data in stage.items():
        if data == value:
            a_dictionary.pop(index)
    return (a_dictionary)
