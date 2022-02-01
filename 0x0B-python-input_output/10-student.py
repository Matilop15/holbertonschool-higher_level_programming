#!/usr/bin/python3
# Matias López <3959@holbertonschool.com>
"""
10-student.py
If attrs is a list of strings, only attribute
names contained in this list must be retrieved.
"""


class Student:
    """
    class student and def, nomb, apellido, age
    """
    def __init__(self, first_name, last_name, age):
        """inicialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return only attribute"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ret = {}
            for p, r in self.__dict__.items():
                if p in attrs:
                    ret[p] = r
                    return ret
        else:
            return self.__dict__
