import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.reverse_array import reverse_array


test_data = [
    ([50, 60, 70, 80, 90], [90, 80, 70, 60, 50]),
    ([50, 60], [60, 50]),
    ([70, 50, 60, 90, 80], [80, 90, 60, 50, 70])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_reverse_array(input_array: List[int], expected_result: List[int]):
    assert expected_result == reverse_array(input_array)
