#!/usr/bin/python3
"""Appending a str at the end of a text file (UTF8),
and returns the no. of chars added"""


def append_write(filename="", text=""):
    """
    Func that appends a string at the end of a text file (UTF8),
    and returns the no. of chars added

    Args:
        filename: Name of the file to open and print
        text: Text to be written
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
