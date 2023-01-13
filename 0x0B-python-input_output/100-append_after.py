#!/usr/bin/python3
"""this module contains a method to Search and append file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after each line
    args:
        filename: name of file to edit
        search_string: search location to edit
        new_string: string to add
    """

    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
