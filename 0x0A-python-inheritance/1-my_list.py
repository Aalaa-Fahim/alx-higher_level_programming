#!usr/bin/python3
"""A module to show inheritance"""


class MyList(list):
    """An inherited class"""
    def print_sorted(self):
        """A method to sort integers"""
        print(sorted(self))
