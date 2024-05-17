#!/usr/bin/python3
"""
Script that reads `stdin` and computes metrics.
"""
import re
import sys
import signal


counter = 0
file_size_accum = {'total': 0}
status_count = {
    status_code: 0 for status_code in [
        200, 301, 400, 401, 403, 404, 405, 500
    ]
}


def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C)
    """
    print_stats()
    sys.exit(0)


def is_valid_line(line):
    """
    Checks if the given line is of the format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> \
    <file size>
    """
    pattern = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Za-z0-9.-]+)| - \['
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET \/projects\/260 HTTP\/1\.1" '
        r'(?:\d+|[A-Za-z]+) (?:\d+|[A-Za-z]+)'
    )
    return pattern.match(line)


def print_stats():
    """
    Prints the statistics.
    """
    print(f'File size: {file_size_accum["total"]}')
    for status_code in sorted(status_count.keys()):
        if status_count[status_code] != 0:
            print(f'{status_code}: {status_count[status_code]}')


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            if is_valid_line(line) is False:
                continue

            line_parts = line.split()
            file_size = int(line_parts[-1])
            status_code = line_parts[-2]

            file_size_accum['total'] += file_size
            if status_code.isdigit() and int(status_code) in status_count:
                status_count[int(status_code)] += 1

            counter += 1
            if counter % 10 == 0:
                print_stats()

        except (IndexError, ValueError):
            continue

    if counter % 10 != 0 or counter == 0:
        print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
