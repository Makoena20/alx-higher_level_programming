#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Class representing a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): A list of strings
        Returns:
            dict: A dictionary representation of the student instance
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Args:
            json (dict): A dictionary containing attributes to reload
        """
        for key, value in json.items():
            setattr(self, key, value)
