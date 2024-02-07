#!/usr/bin/python3
"""Defines load_from_json_file"""
import json


def load_from_json_file(filename):
    """Load Python object from a JSON file.

        Args:
            filename (str): The name of the file containing the JSON data.

        Returns:
            The deserialized Python object.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
