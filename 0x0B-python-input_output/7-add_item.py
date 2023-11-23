#!/usr/bin/python3
"""Script that adds all args to a py list then save them to a file"""
from sys import argv


if __name__ == "__main__":
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"

    try:
        json_list = load_from_json_file(filename)
    except FileNotFoundError:
        json_list = []

    json_list.extend(argv[1:])

    save_to_json_file(json_list, filename)
