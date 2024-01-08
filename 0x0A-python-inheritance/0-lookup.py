#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """It returns the list of available attributes and methods of an object
    Args:
        obj: the object to return as a list.

    Returns:
        list: the list of available attributes and methods.
    """
    return dir(obj)
