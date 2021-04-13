import allure
import pytest
from typing import List
from src.main.java.testAlgo.fox.lesson012.factorization import factor


test_data = [
    (12, [2, 3])
]


@allure.feature('Foxford')
@allure.story('Factorization')
@pytest.mark.parametrize("input,expected_result", test_data)
def test_factorization(input: int, expected_result: List[int]):
    assert expected_result == factor(input)
