#!/usr/bin/python3.8
import dis
import sys

def print_hidden_names():
    if len(sys.argv) != 1:
        return

    with open("hidden_4.pyc", "rb") as file:
        magic_number = file.read(4)
        timestamp = file.read(4)
        code_object = compile(file.read(), '', 'exec')

        names = [name for name in code_object.co_names if not name.startswith('__')]
        names.sort()

        for name in names:
            print(name)

if __name__ == "__main__":
    print_hidden_names()

