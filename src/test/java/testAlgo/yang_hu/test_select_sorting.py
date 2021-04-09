import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.select_sorting import select_sorting


test_data = [
    ([60, 80, 95, 50, 70], [50, 60, 70, 80, 95])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_select_sorting(input_array: List[int], expected_result: List[int]):
    assert expected_result == select_sorting(input_array)
