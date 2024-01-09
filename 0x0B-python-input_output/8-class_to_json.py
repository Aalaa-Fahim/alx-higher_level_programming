#!/usr/bin/python3
"""defining the function class_to_json"""


def class_to_json(obj):
    """method that returns the dictionary description"""
    return obj.__dict__
