#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    new = ""
    for i, c in enumerate(str):
        if i != n:
            new += c
    return new
