#!/usr/bin/python3
"""module for MyList class."""


class MyList(list):
    """An inherited class"""
    def print_sorted(self):
        """A method to sort integers"""
        print(sorted(self))
