#!/usr/bin/env python3
""" Sorting algorithms. """
from random import random
from time import time


def time_measuring(func, input_f, repeat=100):
    """function time measuring."""
    base_time = time()
    for _ in range(repeat):
        func(input_f)
    total_time = time() - base_time
    return total_time


def counting_sort():
    """Counting Sort
    complexity:
        time:
            - best Ω(n+k)
            - average Θ(n+k)
            - worst O(n+k)
        space: worst O(k)
    """


def counting_sort_test():
    """Test counting_sort function.
    time complexity is T(counting_sort) and space S(counting_sort)
    T(random(10)+T(counting_sort(10))+T(sorted(10))
    """
    numbers = [int(random() * 10) for _ in range(10)]
    assert counting_sort(numbers) == sorted(numbers)
