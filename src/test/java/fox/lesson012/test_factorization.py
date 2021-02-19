import pytest


test_data = [
    (12, [2, 3, 4, 6])
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_factorization(input: int, expected_result: List[int]):
    assert expected_result == factor(input)
