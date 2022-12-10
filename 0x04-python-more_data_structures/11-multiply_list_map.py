#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x,y=number: x * y, my_list)))
