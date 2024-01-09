#!/usr/bin/python3
"""defining the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """method to create an Object from a JSON file"""
    with open(filename, "r", encoding='UTF8') as f:
        return json.load(f)
