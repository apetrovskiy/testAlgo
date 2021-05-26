import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.min_value import min_value


test_data = [
    ([60, 80, 95, 50, 70], 50),
    ([50, 80, 95, 60, 70], 50),
    ([60, 80, 95, 70, 50], 50)
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_min_value(input_array: List[int], expected_result: int):
    assert expected_result == min_value(input_array)
