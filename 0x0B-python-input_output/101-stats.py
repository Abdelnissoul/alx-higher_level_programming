#!/usr/bin/python3
"""function Reads from standard input and computes metrics"""


def print_stats(total_size, status_codes_count):
    """Printing metrics by defining the size"""
    print("File size: {}".format(total_size))
    for key in sorted(status_codes_count):
        print("{}: {}".format(key, status_codes_count[key]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes_count = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(total_size, status_codes_count)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes_count.get(line[-2], -1) == -1:
                        status_codes_count[line[-2]] = 1
                    else:
                        status_codes_count[line[-2]] += 1
            except IndexError:
                pass

        print_stats(total_size, status_codes_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes_count)
        raise
