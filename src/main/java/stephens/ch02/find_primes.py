from math import sqrt
from typing import List


def find_primes(max_number: int) -> List[int]:
    is_composite: List[bool] = [False] * (max_number + 1)

    for i in range(4, max_number + 1, 2):
        is_composite[i] = True

    next_prime: int = 3
    stop_at: int = sqrt(max_number)
    while next_prime <= stop_at:
        for i in range(next_prime * 2, max_number + 1, next_prime):
            is_composite[i] = True
        next_prime += 2
        while next_prime <= max_number and is_composite[next_prime]:
            next_prime += 2

    primes: List[int] = []
    for i in range(2, max_number + 1):
        if not is_composite[i]:
            primes.append(i)

    return primes
