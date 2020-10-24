#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Write a class MyInt that inherits from int"""
    def __ne__(self, other):
        """Defines behavior for the equality operator, =="""
        return True

    def __eq__(self, other):
        """Defines behavior for the inequality operator, !="""
        return False
