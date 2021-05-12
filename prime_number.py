#!/usr/bin/env python3
""" Prime numbers. """
from math import sqrt


def is_prime_number(number: int) -> bool:
    """Prime Number."""
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True
