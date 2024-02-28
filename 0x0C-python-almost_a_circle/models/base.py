#!/usr/bin/python3

import json
import csv
import turtle


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes and deserializes in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes from CSV """
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = [int(val) for val in row]
                    if cls.__name__ == "Rectangle":
                        instance = cls(row[1], row[2], row[3], row[4], row[0])
                    elif cls.__name__ == "Square":
                        instance = cls(row[1], row[2], row[3], row[0])
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws all the Rectangles and Squares using Turtle graphics module """
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()

        # Draw Rectangles
        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rect.width)
                pen.right(90)
                pen.forward(rect.height)
                pen.right(90)
            pen.end_fill()
            pen.penup()

        # Draw Squares
        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)
            pen.end_fill()
            pen.penup()

        screen.mainloop()


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns the area of the Rectangle """
        return self.width * self.height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character '#' """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """ Updates the attributes of the Rectangle """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square instance """
        super().__init__(size, size, x, y, id)
        self.size = size

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """ Updates the attributes of the Square """
        if args:
            attrs = ["id", "size", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


if __name__ == "__main__":
    pass
