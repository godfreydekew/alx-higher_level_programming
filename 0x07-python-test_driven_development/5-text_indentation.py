#!/usr/bin/python3
"""Defining a function that tokenizes a text and prints each tokens."""


def text_indentation(text):
    """
       Prints a text with 2 new lines after each delimiter.

       The delimiters are '.', '?', and ':'.

       Args:
           text (str): The input text.

       Raises:
           TypeError: If 'text' is not a string.

       Returns:
           None

       The function iterates through each character in
       the input text and prints the characters.
       When a delimiter ('.', '?', or ':') is encountered,
       the accumulated characters are printed
       with 2 new lines added after the delimiter.
       Leading and trailing whitespaces around each
       printed token are stripped.

    """
    my_str = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        my_str += c
        if c in ['.', '?', ':']:
            print(my_str.strip(), end="\n\n")
            my_str = ""
    print(my_str.strip(), end="")
