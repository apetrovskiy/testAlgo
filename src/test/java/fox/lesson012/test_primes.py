from src.main.java.fox.lesson012.primes import is_prime_number
import pytest


test_data = [
    (13, True),
    (15, False)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_is_prime_number(input: int, expected_result: int):
    assert expected_result == is_prime_number(input)
