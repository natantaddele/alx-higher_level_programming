#!/usr/bin/python3
"""
Module containing the to_json_string function
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object
    """
    import json

    return json.dumps(my_obj)
