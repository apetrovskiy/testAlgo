from src.main.java.testAlgo.durr_vie.CharacterStrings.Anagrams.anagrams \
    import anagrams
from typing import List
import pytest


test_data = [
    ("below the car is a rat drinking cider and bending \
        its elbow while this thing is an arc that can act \
            like a cat which cried during the night caused \
                by pain in its bowel", [
     ['bowel', 'below', 'elbow'], ['arc', 'car'],
        ['night', 'thing'], ['cried', 'cider'], ['act', 'cat']])
]


@allure.feature('Durr Vie')
@allure.story('Anagrams')
@ pytest.mark.parametrize("input,expected_result", test_data)
def test_anagrams(input: str, expected_result: List[str]):
    [x.sort() for x in expected_result]
    expected_result.sort()
    actual_result = anagrams(input)
    [x.sort() for x in actual_result]
    actual_result.sort()
    assert len(actual_result) == len(expected_result)
    assert all([sorted(a) ==
                sorted(b) for a, b in zip(actual_result, expected_result)])
