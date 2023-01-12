#!/usr/bin/python3
"""Module contains a REad file function"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""

    with open(filename, "r", encoding='utf-8') as f:
        file_data = f.read()
        print(file_data, end='')
