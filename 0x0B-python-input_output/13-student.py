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

    def to_json(self, attrs=None):
        """[summary]

        Args:
            attrs ([list]): if the value exist then return as dict.
            Defaults to None.

        Returns:
            [dict]: dict
        """
        my_dict = {}
        if attrs is not None:
            if type(attrs) is list:
                for value in attrs:
                    if type(value) != str:
                        return self.__dict__
                    if value in self.__dict__.keys():
                        my_dict[value] = self.__dict__[value]
                return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Write a class Student that defines a student by

        Args:
            json ([json]): update all dict

        Returns:
            [dict]: dict
        """
        return self.__dict__.update(json)
