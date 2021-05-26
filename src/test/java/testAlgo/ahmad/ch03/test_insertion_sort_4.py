import pytest
from typing import List
from src.main.java.testAlgo.ahmad.ch03.insertion_sort_4 import insertion_sort


test_data = [
    ([25, 26, 22, 24, 27, 23, 21], [21, 22, 23, 24, 25, 26, 27])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_insertion_sort(input_array: List[int], expected_result: List[int]):
    assert expected_result == insertion_sort(input_array)
