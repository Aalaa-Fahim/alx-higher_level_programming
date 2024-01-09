#!/usr/bin/python3
"""module for a class Student"""


class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """A constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that retrieves a dictionary representation"""
        try:
            for a in attrs:
                if type(a) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """A method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self..__dict__[key] = value
