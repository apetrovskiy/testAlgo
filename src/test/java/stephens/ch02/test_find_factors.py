from src.main.java.stephens.ch02.find_factors import version01
from typing import List
import pytest


test_data = [
    (4, [2, 2]),
    (10, [2, 5]),
    (125, [5, 5, 5])
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_find_factors(input: int, expected_result: List[int]):
    assert expected_result == version01(input)
