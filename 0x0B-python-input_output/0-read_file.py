#!/usr/bin/python3
"""Function reads a text file and prints it"""


def read_file(filename=""):
    """Reads UTF8 a text file and prints it out"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
