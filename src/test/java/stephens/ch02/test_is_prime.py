from src.main.java.stephens.ch02.is_prime import is_prime
import pytest


test_data = [
    (5, 10, True),
    (6, 2, False),
    (27, 5, False),
    (37, 20, True)
]


@pytest.mark.parametrize("number,tests_number,expected_result", test_data)
def test_is_prime(number: int, tests_number: int, expected_result: bool):
    assert expected_result == is_prime(number, tests_number)
