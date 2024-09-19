#!/usr/bin/python3

"""
Minimum Operations Module

This module contains a function that
calculates the minimum number of operations
needed to reach a target number of characters in a file, starting
with a single character.
The only operations allowed are 'Copy All' and 'Paste'.
"""

import math


def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n
    'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations required to achieve n characters.
    """

    # Check if n is less than or equal to 1, where the task is impossible
    if n <= 1:
        return 0

    # Initialize the operations count
    operations = 0

    # Iterate through potential factors of n, starting from 2
    for i in range(2, int(math.sqrt(n)) + 1):
        # While n is divisible by i, divide n by i and
        # increment operations count
        while n % i == 0:
            operations += i
            n //= i

    # If n is a prime number, add it to the operations count
    if n > 1:
        operations += n

    return operations
