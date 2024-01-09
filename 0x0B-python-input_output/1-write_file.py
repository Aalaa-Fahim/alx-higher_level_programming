#!/usr/bin/python3
"""defining a function that writes a text file"""


def write_file(filename="", text=""):
    """A method to overwrite a file"""
    with open(filename, "w", encoding='UTF8') as f:
        return f.write(text)
