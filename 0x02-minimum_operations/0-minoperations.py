#!/usr/bin/python3
"""
The minimum operations coding challenge.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n H characters in the file.

    :param n: Number of H characters to achieve
    :return: Integer representing the fewest number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
