from src.main.java.testAlgo.stephens.ch02.find_primes import find_primes
from typing import List
import pytest


test_data = [
    (4, [2, 3]),
    (10, [2, 3, 5, 7]),
    (125, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
           59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]),
    (127, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
           59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127])
]


@allure.feature('Stephens')
@allure.story('Find primes')
@pytest.mark.parametrize("input,expected_result", test_data)
def test_find_primes(input: int, expected_result: List[int]):
    assert expected_result == find_primes(input)
