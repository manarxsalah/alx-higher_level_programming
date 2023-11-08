#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """custom MyList class"""
    def print_sorted(self):
        """Method for printing"""
        print(sorted(self))
