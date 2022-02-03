#!/usr/bin/python3
# Matias Lópezz <3959@holbertonschool.com>
"""
Write the first class Base
private class attribute __nb_objects = 0
"""


class Base:
    """
    base de todo
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        if id is None increment __nb_objects
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id  = id                      
