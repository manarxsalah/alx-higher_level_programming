#!/usr/bin/python3
"""Writing a str to a text file (UTF8) and returns the no. of chars written"""


def write_file(filename="", text=""):
    """
    Func writes a str to a text file (UTF8),
    and returns the no. of chars written

    Args:
        filename: Name of the file to open and print
        text: The text to be written
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
