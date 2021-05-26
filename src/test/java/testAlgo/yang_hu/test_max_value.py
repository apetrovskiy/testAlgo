import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.max_value import max_value


test_data = [([60, 50, 95, 80, 70], 95)]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_max_value(input_array: List[int], expected_result: int):
    assert expected_result == max_value(input_array)
