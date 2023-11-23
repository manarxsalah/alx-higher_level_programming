#!/usr/bin/python3
"""Func that writes an Object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Func that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to be saved as json str
        filename: The json filename
    """
    with open(filename, "w", encoding="utf-8") as jsonFile:
        json.dump(my_obj, jsonFile)
