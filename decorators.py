#!/usr/bin/env python3
""" Decorators."""
from time import time
from functools import wraps


def time_function(fn):
    """Measuring time a functions."""

    @wraps(fn)
    def measure_time(*args, **kwargs):
        time_1 = time()
        result = fn(*args, **kwargs)
        time_2 = time()
        print(
            f"[!] @time_function {fn.func_name} took {str( time_2 - time_1 )} seconds"
        )

    return measure_time
