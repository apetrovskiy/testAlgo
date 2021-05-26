import allure
from src.main.java.testAlgo.stephens.ch02.find_factors \
    import version01, version02
from typing import List
import pytest


test_data = [
    (4, [2, 2]),
    (10, [2, 5]),
    (125, [5, 5, 5]),
    (127, [127])
]


@allure.feature('Stephens')
@allure.story('Find factors, v1')
@pytest.mark.parametrize("input,expected_result", test_data)
def test_find_factors_version01(input: int, expected_result: List[int]):
    assert expected_result == version01(input)


@allure.feature('Stephens')
@allure.story('Find factors, v2')
@pytest.mark.parametrize("input,expected_result", test_data)
def test_find_factors_version02(input: int, expected_result: List[int]):
    assert expected_result == version02(input)
