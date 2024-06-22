from typing import List

import allure
import pytest

from src.main.java.testAlgo.fox.lesson012.primes import is_prime_number

test_data = [(13, True), (15, False)]

test_data_for_series = [(35, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])]

test_data_for_sum = [(32, 4096, 1069931)]


@allure.feature("Foxford")
@allure.story("Is prime number")
@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_is_prime_number(input_data: int, expected_result: bool):
    assert expected_result == is_prime_number(input_data)


@allure.feature("Foxford")
@allure.story("Primes series")
@pytest.mark.parametrize("input_data,expected_result", test_data_for_series)
def test_primes_series(input_data: int, expected_result: List[int]):
    assert expected_result == [x for x in range(2, input_data) if is_prime_number(x)]


@allure.feature("Foxford")
@allure.story("Primes sum")
@pytest.mark.parametrize("start,end,expected_result", test_data_for_sum)
def test_primes_sum(start: int, end: int, expected_result: int):
    assert expected_result == sum(
        [x for x in range(start, end + 1) if is_prime_number(x)]
    )
