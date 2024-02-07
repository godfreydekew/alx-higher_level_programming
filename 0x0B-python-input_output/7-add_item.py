#!/usr/bin/python3
"""Script for saving and loading data using JSON files.

Usage:
    Execute the script with additional command-line arguments,
    and the script will save those arguments to a JSON
    file named "add_item.json".
    The saved data can be loaded back using the
    load_from_json_file function.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        new_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        new_list = []
    new_list.extend(sys.argv[1:])
    save_to_json_file(new_list, "add_item.json")
