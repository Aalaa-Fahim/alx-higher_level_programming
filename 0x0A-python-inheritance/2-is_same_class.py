#!/usr/bin/python3
"""A module to test inheritance"""


def is_same_class(obj, a_class):
    """A method to check if the object is exactly an instance of the specified class
    Args:
    obj: the object to be checked
    a_class: the specified class to check in

    Return:
    True or false
    """
    return isinstance(obj, a_class)
