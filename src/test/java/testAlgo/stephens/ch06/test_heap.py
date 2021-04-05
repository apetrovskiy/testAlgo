import pytest
from typing import List
from src.main.java.testAlgo.stephens.ch06.heap import array_to_heap


test_data = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15],
     #  [15, 11, 12, 7, 5, 10, 2, 6, 4, 3, 1, 8, 9]),
     [15, 11, 12, 9, 10, 6, 7, 8, 4, 2, 5, 3, 1]),
    ([4, 10, 3, 5, 1], [10, 5, 3, 4, 1]),
    ([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17], [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_heap(input_array: List[int], expected_result: List[int]):
    assert expected_result == array_to_heap(input_array)
