#!/usr/bin/python3
"""Defines save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Save Python object to a JSON file.

       Args:
           my_obj: The Python object to be serialized and saved.
           filename (str): The name of the file to
            save the JSON data.

       Returns:
           None
       """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
