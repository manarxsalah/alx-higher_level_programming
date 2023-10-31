#!/usr/bin/python3
"""Def a locked class"""


class LockedClass:
    """
    Prevents the usr from istantiating new LockedClass attributes
    for everything other than attributes called 'first_name'
    """

    __slots__ = ["first_name"]
