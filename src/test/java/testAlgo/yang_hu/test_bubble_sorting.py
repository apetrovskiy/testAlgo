import allure
import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.bubble_sorting import bubble_sorting


test_data = [
    ([60, 50, 95, 80, 70], [50, 60, 70, 80, 95]),
    ([95, 50, 60, 80, 70], [50, 60, 70, 80, 95]),
    ([60, 70, 95, 80, 50], [50, 60, 70, 80, 95]),
    ([95, 80, 70, 60, 50], [50, 60, 70, 80, 95]),
    ([50, 60, 70, 80, 95], [50, 60, 70, 80, 95]),
]


@allure.feature("Yang Hu")
@allure.story("Bubble sorting")
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_bubble_sorting(input_array: List[int], expected_result: List[int]):
    assert expected_result == bubble_sorting(input_array)
