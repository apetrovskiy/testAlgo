import pytest
from typing import List
from src.main.java.testAlgo.stephens.ch06.select_sorting_2 import select_sorting


test_data = [
    ([7, 5, 6, 1, 3, 2, 8, 0], [0, 1, 2, 3, 5, 6, 7, 8])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_select_sorting_2(input_array: List[int], expected_result: List[int]):
    assert expected_result == select_sorting(input_array)
