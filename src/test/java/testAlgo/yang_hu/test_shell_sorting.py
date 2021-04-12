import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.shell_sorting import shell_sorting


test_data = [
    ([9, 6, 5, 8, 0, 7, 4, 3, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_shell_sorting(input_array: List[int], expected_result: List[int]):
    assert expected_result == shell_sorting(input_array)
