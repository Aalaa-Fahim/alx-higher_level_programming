#!/usr/bin/python3
"""module to add arguments to a list then save them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = list(sys.argv[1:])

try:
    predata = load_from_json_file('add_item.json')
except Exception:
    predata = []

predata.extend(arg_list)
save_to_json_file(predata, 'add_item.json')
