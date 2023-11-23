#!/usr/bin/python3
"""Func that returns an object represented by a JSON str"""
import json


def from_json_string(my_str):
    """
    Func that returns an object represented by a JSON string

    Args:
        my_str: The json str to be returned as object
    """
    return json.loads(my_str)
