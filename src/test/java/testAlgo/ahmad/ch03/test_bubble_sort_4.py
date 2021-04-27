import pytest
from typing import List
from src.main.java.testAlgo.ahmad.ch03.bubble_sort_4 import bubble_sort


test_data = [
    ([25, 21, 22, 24, 23, 27, 26], [21, 22, 23, 24, 25, 26, 27])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_bubble_sort(input_array: List[int], expected_result: List[int]):
    assert expected_result == bubble_sort(input_array)
