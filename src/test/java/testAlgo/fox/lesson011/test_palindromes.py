import allure
import pytest
from src.main.java.testAlgo.fox.lesson011.palindromes import is_palindrome


test_data = [
    ("aaa", True),
    ("aaab", False),
    ("", True),
    ("a", True)
]


@allure.feature('Foxford')
@allure.story('Palindrome')
@pytest.mark.parametrize("input,expected_result", test_data)
def test_is_palindrome(input: str, expected_result: bool):
    assert expected_result == is_palindrome(input)
