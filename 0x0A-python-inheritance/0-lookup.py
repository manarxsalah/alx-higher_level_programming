#!/usr/bin/python3
"""Lookup method"""


def lookup(obj):
    """Lookup object attributes
    Args:
        obj: the object to list
    Returns:
        list: thr list of attributes
    """
    return dir(obj)
