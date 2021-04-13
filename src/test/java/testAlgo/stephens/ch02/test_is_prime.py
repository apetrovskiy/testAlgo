from src.main.java.testAlgo.stephens.ch02.is_prime import is_prime
import pytest


test_data = [
    (5, 100, True),
    (6, 2, False),
    (27, 5, False),
    (37, 100, True)
]


@allure.feature('Stephens')
@allure.story('Is prime')
@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("number,tests_number,expected_result", test_data)
def test_is_prime(number: int, tests_number: int, expected_result: bool):
    assert expected_result == is_prime(number, tests_number)
