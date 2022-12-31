#!/usr/bin/python3

"""
Text indentation
"""


def text_indentation(text):
    """
    Text indentation prints a text with 2 new lines after each of the cases:
    ., ? and :
    Args:
        @text: string to be edited

    Return:
        No returns

    Exception:
        TypeError: text must be a string
    """

    new_line = False
    new_line_char = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if new_line:
            if i == ' ':
                continue
            else:
                print('\n', end='\n')
                new_line = False
        print(i, end='')
        if i in new_line_char:
            new_line = True
