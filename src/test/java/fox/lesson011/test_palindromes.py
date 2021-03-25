from src.main.java.fox.lesson011.palindromes import is_palindrome
import pytest


test_data = [
    ("aaa", True),
    ("aaab", False),
    ("", True),
    ("a", True)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_is_palindrome(input: str, expected_result: bool):
    assert expected_result == is_palindrome(input)