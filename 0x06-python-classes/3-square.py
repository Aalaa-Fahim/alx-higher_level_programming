#!/usr/bin/python3
"""A Square module."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0):
        """Method.

        Args:
            size: the length of a side of the square.

        Raises:
            TypeError: if the size is not an integer value
            ValueError: if the size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area of this square.

        Returns:
            the size squared.
        """
        return self.__size ** 2
