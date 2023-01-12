#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if __name__ == '__main__':
    try:
        lst = loadfile("add_item.json")
    except:
        lst = []
    for i in range(1, len(sys.argv)):
        lst.append(sys.argv[i])
    savefile(lst, "add_item.json")
