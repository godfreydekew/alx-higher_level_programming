#!/usr/bin/python3
"""Defines from_json_string"""
import json


def from_json_string(my_str):
    """
    Convert from json to object
    :param my_str:
    json string
    :return:
    object represented by the json string
    """
    return json.loads(my_str)
