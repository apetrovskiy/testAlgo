from math import sqrt
from typing import List


def version01(number: int) -> List[int]:
    factors: List[int] = []
    i: int = 2
    while i < number:
        while number % i == 0:
            factors.append(i)
            number = number / i
        i += 1
    if number > 1:
        factors.append(number)
    return factors


def version02(number: int) -> List[int]:
    factors: List[int] = []

    while number % 2 == 0:
        factors.append(2)
        number = number / 2

    i: int = 3
    max_factor: int = sqrt(number)
    while i <= max_factor:
        while number % i == 0:
            factors.append(i)
            number = number / i
            max_factor = sqrt(number)
        i += 2
    if number > 1:
        factors.append(number)
    return factors
