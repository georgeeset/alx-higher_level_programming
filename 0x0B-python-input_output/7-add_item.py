#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


arg_list = []
if os.path.exists("add_item.json"):
    arg_list = load_file("add_item.json")

for arg in sys.argv[1:]:
        arg_list.append(arg)

save_file(arg_list, "add_item.json")
