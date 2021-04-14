import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.merge_sort import combine, merge_sort


test_data = [
    ([35, 12, 24, 29, 13, 1, 45, 3], [1, 3, 12, 13, 24, 29, 35, 45])
]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_merge_sort(input_array: List[int], expected_result: List[int]):
    print(f"expected = {expected_result}")
    actual_result = merge_sort(input_array)
    print(f"actual = {actual_result}")
    # assert expected_result == merge_sort(input_array)
    assert expected_result == actual_result


test_data_arrays = [
    ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([5, 6, 2, 1], [56, 3, 7, 4], [1, 2, 3, 4, 5, 6, 7, 56])
]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("input1,input2,expected_result", test_data_arrays)
def test_combine(input1: List[int], input2: List[int], expected_result: List[int]):
    assert expected_result == combine(input1, input2)
