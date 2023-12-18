"""
Starting and stopping individual Process instances involves a lot of overhead. The 
most common use case is to have a pool of workers and assign tasks to them.

When the two processes 
are reading and writing a file, and running concurrently, we have to be sure the 
reader is waiting for the writer to produce data.

TODO: Need to understand this better!
"""

from __future__ import annotations
from math import sqrt, ceil
import random
from multiprocessing.pool import Pool


def prime_factors(value: int) -> list[int]:
    if value in {2, 3}:
        return [value]
    factors: list[int] = []
    for divisor in range(2, ceil(sqrt(value)) + 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend((prime_factors(divisor)))
            factors.extend(prime_factors(quotient))
            break
    else:
        factors = [value]

    return factors


if __name__ == "__main__":
    to_factor = [random.randint(100_000_000, 1_000_000_000) for i in range(40_960)]
    with Pool() as pool:
        # map the function to a list of arguments that will be run as individual processes
        results = pool.map(prime_factors, to_factor)

    primes = [
        value for value, factor_list in zip(to_factor, results) if len(factor_list) == 1
    ]
    print(f"9-digit primes: {primes}")
