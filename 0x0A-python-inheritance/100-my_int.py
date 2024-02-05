#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A MyInt class"""
    def __eq__(self, other):
        """Overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts != operator"""
        return int(self) == int(other)
