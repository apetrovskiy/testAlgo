from src.main.java.durr_vie.CharacterStrings.TextOn9Keys.text_on_9_keys import text_on_9_keys
import pytest


test_data = [(2665687, 'bonjour')]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_text_on_9_keys(input: int, expected_result: str):
    assert expected_result == text_on_9_keys(input)
