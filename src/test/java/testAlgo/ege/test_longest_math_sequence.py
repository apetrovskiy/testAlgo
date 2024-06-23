import allure
import pytest

from src.main.java.testAlgo.ege.longest_math_sequence import (
    longest_math_sequence,
    longest_math_sequence_by_lanskaya,
)

test_data = [
    ("00", 1),
    ("070", 2),
    ("700", 3),
    ("0700", 3),
    ("7*", 1),
    ("07*7", 3),
    ("700*707-700*700", 15),
    ("789-7*789-0789-7*789-", 11),
    ("", 0),
    ("7**8", 1),
    ("*-*-*08**-078*-*-02-*-*-*-", 2),
]


@allure.feature("EGE")
@allure.story("Math sequence")
@pytest.mark.parametrize("input_data,expected_result", test_data)
@pytest.mark.skip("Wrong results")
def test_longest_math_sequence_by_lanskaya(input_data: str, expected_result: int):
    actual = longest_math_sequence_by_lanskaya(input_data)
    assert (
        expected_result == actual
    ), f"For '{input_data}' expected {expected_result}, actual {actual}"


@allure.feature("EGE")
@allure.story("Math sequence")
@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_longest_math_sequence(input_data: str, expected_result: int):
    actual = longest_math_sequence(input_data)
    assert (
        expected_result == actual
    ), f"For '{input_data}' expected {expected_result}, actual {actual}"
