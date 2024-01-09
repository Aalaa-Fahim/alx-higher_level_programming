#!/usr/bin/python3
"""defining a function for the JSON representation"""
import json


def to_json_string(my_obj):
    """method to return the JSON representation of an object"""
    return json.dumps(my_obj)
