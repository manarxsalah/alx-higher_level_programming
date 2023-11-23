#!/usr/bin/python3
"""Function that returns the dictionary description
for JSON serialization of an object"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    for JSON serialization of an object

    Args:
        obj: Instance of a class
    """
    obj_dict = {}

    if "__dict__" in dir(obj):
        obj_dict = obj.__dict__.copy()

    return obj_dict
