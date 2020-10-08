#!/usr/bin/python3
"""Write a class Student that defines a student by

    Returns:
        [type]: [dict]
"""


class Student:
    """Write a class Student that defines a student by
    """
    def __init__(self, first_name, last_name, age):
        """Write a class Student that defines a student by

        Args:
            first_name ([str]):
            last_name ([str]):
            age ([int]):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Write a class Student that defines a student by

            Returns:
            [type]: [dict]
        """
        return self.__dict__
