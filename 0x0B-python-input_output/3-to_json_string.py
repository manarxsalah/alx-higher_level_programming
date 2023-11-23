#!/usr/bin/python3
"""Module of JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Func that returns the JSON representation of an object

    Args:
        my_obj: Object to be returned as json str representation
    """
    return json.dumps(my_obj)
