from src.main.java.testAlgo.durr_vie.CharacterStrings. \
    TextOn9Keys.text_on_9_keys import text_on_9_keys
import pytest


test_data = [(2665687, 'bonjour')]


@allure.feature('Durr Vie')
@allure.story('T9')
@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("input,expected_result", test_data)
def test_text_on_9_keys(input: int, expected_result: str):
    assert expected_result == text_on_9_keys(input)
