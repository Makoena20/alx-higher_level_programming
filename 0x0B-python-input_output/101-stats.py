#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

def print_stats(total_size, status_codes):
    """Prints the computed statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    """Main function to read stdin and compute metrics."""
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        line_count = 0
        for line in sys.stdin:
            try:
                parts = line.split()
                size = int(parts[-1])
                status_code = parts[-2]
                total_size += size
                status_codes[status_code] += 1
                line_count += 1
            except (IndexError, ValueError):
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
