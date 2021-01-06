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
