#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
