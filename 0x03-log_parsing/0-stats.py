#!/usr/bin/python3
"""
Script that reads `stdin` and computes metrics.
"""
import re
import sys


def is_valid_line(line):
    """
    Checks if the given line is of the format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> \
    <file size>
    """
    pattern = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET \/projects\/260 HTTP\/1\.1" '
        r'(200|301|400|401|403|404|405|500) \d+'
    )
    return pattern.match(line)


def print_stats(status_count):
    """
    Prints the statistics.
    """
    print(f'File size: {file_size_accum["total"]}')
    for status_code in sorted(status_count.keys()):
        if status_count[status_code] != 0:
            print(f'{status_code}: {status_count[status_code]}')


counter = 0
file_size_accum = {'total': 0}
status_count = {}
for code in [200, 301, 400, 401, 403, 404, 405, 500]:
    status_count[code] = 0

for line in sys.stdin:
    try:
        if is_valid_line(line) is False:
            continue
        line_parts = line.rstrip().split()
        file_size = int(line_parts[-1])
        status_code = int(line_parts[-2])
        file_size_accum['total'] += file_size

        if status_code in status_count:
            status_count[status_code] += 1

        counter += 1
        if counter % 10 == 0:
            print_stats(status_count)

    except KeyboardInterrupt:
        print_stats(status_count)
