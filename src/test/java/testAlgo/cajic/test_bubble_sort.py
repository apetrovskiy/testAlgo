import allure
import pytest
from typing import List
from src.main.java.testAlgo.cajic.bubble_sort import bubble_sort


test_data = [
    ([3, 7, 1, 4, 6, 5], [1, 3, 4, 5, 6, 7]),
    ([7, 3, 1, 4, 6, 5], [1, 3, 4, 5, 6, 7]),
    ([3, 7, 5, 4, 6, 1], [1, 3, 4, 5, 6, 7]),
    ([7, 6, 1, 4, 3, 5], [1, 3, 4, 5, 6, 7]),
    ([1, 3, 4, 5, 6, 7], [1, 3, 4, 5, 6, 7]),
    ([7, 6, 5, 4, 3, 1], [1, 3, 4, 5, 6, 7])
]


@allure.feature('Sorting - Cajic')
@allure.story('Bubble sort')
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_bubble_sort(input_array: List[int], expected_result: List[int]):
    assert expected_result == bubble_sort(input_array)
