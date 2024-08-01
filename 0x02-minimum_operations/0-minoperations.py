#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """Minimum number of operations"""
    if n <= 1:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        operations += 1
    return operations


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))