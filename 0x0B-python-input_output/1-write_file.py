#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """Writes text to the file filename"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
