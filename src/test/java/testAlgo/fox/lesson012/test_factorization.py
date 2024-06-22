from typing import List

import allure
import pytest

from src.main.java.testAlgo.fox.lesson012.factorization import factor

test_data = [(12, [2, 3])]


@allure.feature("Foxford")
@allure.story("Factorization")
@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_factorization(input_data: int, expected_result: List[int]):
    assert expected_result == factor(input_data)
