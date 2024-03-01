#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints statistics since the beginning:
- Total file size: File size: <total size>
- Number of lines by status code:
  possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
  format: <status code>: <number>
  status codes are printed in ascending order
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_count[status_code] += 1
            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_count.keys()):
                    if status_count[code] > 0:
                        print("{}: {}".format(code, status_count[code]))

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))
