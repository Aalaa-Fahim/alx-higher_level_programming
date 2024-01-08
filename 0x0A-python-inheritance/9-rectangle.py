#!/usr/bin/python3
"""module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle subclass"""
    def __init__(self, width, height):
        """A constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """A method to compute the area"""
        return self.__width * self.__height

    def str():
        """A method to represent string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
