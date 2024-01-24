#!/usr/bin/python3
import dis
import types
import sys
import marshal

def print_hidden_names(filename):
    with open(filename, 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code = marshal.load(file)

    names = set()
    for instruction in code.co_code:
        if isinstance(instruction, types.CodeType):
            names.update(instruction.co_names)

    filtered_names = sorted(name for name in names if not name.startswith('__'))

    for name in filtered_names:
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <hidden_4.pyc>")
        sys.exit(1)

    filename = sys.argv[1]
    print_hidden_names(filename)

