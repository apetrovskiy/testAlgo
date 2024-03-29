import pytest
from typing import List
from src.main.java.testAlgo.stephens.ch06.insert_sorting_2 import insert_sorting


test_data = [([7, 5, 6, 1, 3, 2, 8, 0], [0, 1, 2, 3, 5, 6, 7, 8])]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_insert_sorting_2(input_array: List[int], expected_result: List[int]):
    assert expected_result == insert_sorting(input_array)
