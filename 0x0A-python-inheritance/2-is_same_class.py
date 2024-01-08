#!/usr/bin/python3
"""A module to test inheritance"""


def is_same_class(obj, a_class):
    """method to check if the object is exactly an instance of specified class
    Args:
        obj: the object to be checked
        a_class: the specified class to check in

    Returns:
        True or false
    """
    return type(obj) == a_class
