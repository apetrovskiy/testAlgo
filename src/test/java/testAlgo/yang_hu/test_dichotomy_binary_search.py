import pytest
from typing import List
from src.main.java.testAlgo.yang_hu.dichotomy_binary_search \
    import dichotomy_binary_search


test_data = [
    ([30, 40, 50, 70, 85, 90, 100], 50, 2),
    ([30, 40, 50, 70, 85, 90, 100], 70, 3),
    ([30, 40, 50, 70, 85, 90, 100], 30, 0),
    ([30, 40, 50, 70, 85, 90, 100], 100, 6),
    ([30, 40, 50, 70, 85, 90, 100], 90, 5)
]


@pytest.mark.parametrize("input_array,search_value,expected_result", test_data)
def test_dichotomy_binary_search(input_array: List[int],
                                 search_value: int, expected_result: int):
    assert expected_result == dichotomy_binary_search(
        input_array, search_value)
