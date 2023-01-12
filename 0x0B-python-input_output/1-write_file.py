#!/usr/bin/python3
"""Module writes to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns num chars written
    args:
        filename: name of the file to write
        text: content string to write to file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
