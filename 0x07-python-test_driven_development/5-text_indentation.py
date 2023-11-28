#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Text indentation method
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while (i < length):
        if text[i] in (".", "?", ":"):
            if (i + 1) != length:
                s = text[i + 1]
                if (s != '.' and s != '?' and s != ':'):
                    print(text[i], end='\n\n')
                    if s == ' ':
                        i += 2
                    if s != ' ':
                        i += 1
        else:
            print(text[i], end='')
            i += 1
