from src.main.java.durr_vie.CharacterStrings.Anagrams.anagrams import anagrams
from typing import List
import pytest


test_data = [
    ("below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel1", [
     ['bowel', 'below', 'elbow'], ['arc', 'car'], ['night', 'thing'], ['cried', 'cider'], ['act', 'cat']])
]


@ pytest.mark.parametrize("input,expected_result", test_data)
def test_anagrams(input: str, expected_result: List[str]):
    assert expected_result == anagrams(input)
