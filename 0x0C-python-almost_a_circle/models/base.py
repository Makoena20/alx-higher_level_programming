#!/usr/bin/python3
"""Base module"""

import json
import csv
import turtle

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**dic) for dic in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV format and writes to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file to list of instances"""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(x) for x in row]
                if cls.__name__ == "Rectangle":
                    instance = cls.create(width=row[1], height=row[2], x=row[3], y=row[4], id=row[0])
                elif cls.__name__ == "Square":
                    instance = cls.create(size=row[1], x=row[2], y=row[3], id=row[0])
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares using Turtle graphics"""
        turtle.reset()
        turtle.title("Shapes Drawing")
        turtle.bgcolor("white")
        turtle.speed(0)
        
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()
        
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()
        
        turtle.hideturtle()
        turtle.done()


