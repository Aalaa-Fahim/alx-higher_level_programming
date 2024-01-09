#!/usr/bin/python3
"""defining a function that appends a text file"""


def append_write(filename="", text=""):
    """A method to append a string at a file"""
    with open(filename, "a", encoding='UTF8') as f:
        return f.write(text)
