import pytest
from typing import List
from src.main.java.testAlgo.stephens.ch06.quick_sorting_2 \
    import quick_sorting


test_data = [
    ([0, 1, 2, 4, 5, 6, 3, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_quick_sorting_2(input_array: List[int], expected_result: List[int]):
    assert expected_result == quick_sorting(input_array)
