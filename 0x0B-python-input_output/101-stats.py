#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            try:
                status = data[-2]
                if status in status_codes:
                    status_codes[status] += 1
                total_size += int(data[-1])
            except ValueError:
                pass

        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for key in sorted(status_codes.keys()):
                if status_codes[key] != 0:
                    print("{}: {}".format(key, status_codes[key]))
            sys.stdout.flush()

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))

