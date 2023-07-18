import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.insert_sorting import insert_sorting


test_data = [
    ([80, 70, 60, 50, 95], [50, 60, 70, 80, 95]),
    ([95, 70, 60, 50, 80], [50, 60, 70, 80, 95]),
    ([80, 70, 60, 95, 50], [50, 60, 70, 80, 95]),
    ([95, 80, 70, 60, 50], [50, 60, 70, 80, 95]),
    ([50, 60, 70, 80, 95], [50, 60, 70, 80, 95]),
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_insert_sorting(input_array: List[int], expected_result: List[int]):
    assert expected_result == insert_sorting(input_array)
