#!/usr/bin/python3
"""defining a function that reads a text file"""


def read_file(filename=""):
    """A method to read file and print it"""
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
