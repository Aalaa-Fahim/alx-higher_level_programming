#!/usr/bin/python3
"""defining the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """method to write an Object to a text file using  JSON"""
    with open(filename, "w", encoding='UTF8') as f:
        json.dump(my_obj, f)
