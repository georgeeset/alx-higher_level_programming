#!/usr/bin/python3
def remove_char_at(str, n):
    strng = ''
    for i in range(len(str)):
        if i != n:
            strng += str[i]
    return (strng)
