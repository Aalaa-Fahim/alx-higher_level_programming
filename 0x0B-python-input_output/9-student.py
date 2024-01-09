#!/usr/bin/python3
"""module for a class Student"""


class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """A constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method that retrieves a dictionary representation"""
        return self.__dict__
