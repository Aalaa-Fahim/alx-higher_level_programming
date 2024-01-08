#!/usr/bin/python3
"""module for Rectangle class"""


class Rectangle(BaseGeometry):
    """A Rectangle subclass"""
     def __init__(self, width, height):
         """A constructor"""
         self.__width = width
         self.__height = height
         self.integer_validator("width", width)
         self.integer_validator("height", height)
