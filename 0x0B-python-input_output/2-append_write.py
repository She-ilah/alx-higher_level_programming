#!/usr/bin/python3
"""Function appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Returns number of characters added to UTF8"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
