#!/usr/bin/python3
"""Defines append_write function"""


def append_write(filename="", text=""):
    """Appends string   to the file filename
    returns:
        number of characters appended
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
