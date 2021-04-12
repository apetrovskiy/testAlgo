import pytest
from typing import List
from src.main.java.testAlgo.stephens.ch06.insert_sorting import insert_sorting


test_data = [
    ([], [])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_insert_sorting_2(input_array: List[int], expected_result: List[int]):
    assert expected_result == insert_sorting(input_array)
