#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1): print("{:c}".format(c), end='') if c not in [ord('e'), ord('q')] else None

