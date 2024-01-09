#!/usr/bin/python3
"""module for defining append_after func"""


def append_after(filename="", search_string="", new_string=""):
    """A method that inserts a line of text to a file"""
    with open(filename, "r", encoding='UTF8') as f:
        lines = f.readlines()
    with open(filename, "w", encoding='UTF8') as f:
        for line in lines:
            if search_string in line:
                f.write(line.rstrip() + " " + new_string + "\n")
            else:
                f.write(line)
