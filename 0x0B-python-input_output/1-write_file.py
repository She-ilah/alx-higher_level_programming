#!/usr/bin/python3
"""Function  writes a string to a text file"""


def write_file(filename="", text=""):
    """Returns the number of characters written in UTF8"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
