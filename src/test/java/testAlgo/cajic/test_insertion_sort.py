import allure
import pytest
from typing import List
from src.main.java.testAlgo.cajic.insertion_sort import insertion_sort


test_data = [
    ([4, 7, 1, 2, 8, 5], [1, 2, 4, 5, 7, 8]),
    ([7, 4, 1, 2, 8, 5], [1, 2, 4, 5, 7, 8]),
    ([4, 7, 5, 2, 8, 1], [1, 2, 4, 5, 7, 8]),
    ([7, 8, 5, 4, 2, 1], [1, 2, 4, 5, 7, 8]),
    ([8, 7, 5, 4, 2, 1], [1, 2, 4, 5, 7, 8]),
    ([1, 2, 4, 5, 7, 8], [1, 2, 4, 5, 7, 8]),
]


@allure.feature("Sorting - Cajic")
@allure.story("Insertion sort")
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_insertion_sort(input_array: List[int], expected_result: List[int]):
    assert expected_result == insertion_sort(input_array)
