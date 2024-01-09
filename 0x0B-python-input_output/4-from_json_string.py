#!/usr/bin/python3
"""defining the function from_json_string"""
import json


def from_json_string(my_str):
    """method to return an object represented by a JSON string"""
    return json.loads(my_str)
