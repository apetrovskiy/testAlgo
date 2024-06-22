import allure
import pytest

from src.main.java.testAlgo.ege.longest_math_sequence import (
    longest_math_sequence_by_lanskaya,
)

test_data = [
    ("00", 1),
    ("01*1", 3),
    ("123-4*324-0123-4*324-", 11),
    ("", 0),
    ("1**2", 1),
]


@allure.feature("EGE")
@allure.story("Math sequence")
@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_longest_math_sequence_by_lanskaya(input_data: str, expected_result: int):
    actual = longest_math_sequence_by_lanskaya(input_data)
    assert (
        expected_result == actual
    ), f"For '{input_data}' expected {expected_result}, actual {actual}"
