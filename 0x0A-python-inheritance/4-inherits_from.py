#!/usr/bin/python3
"""A module to test inheritance"""


def inherits_from(obj, a_class):
    """check if the object is instance of a class that inherited from
    Args:
        obj: the object to be checked
        a_class: the specified class to check in

    Return:
        True or false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
