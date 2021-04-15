import allure
import pytest
from src.main.java.testAlgo.fox.lesson011.towers import move


test_data = [
    (3, 1, 3, 2),
    (4, 1, 3, 2),
    (5, 1, 3, 2)  # ,
    # (20, 1, 3, 2)
]


@allure.feature('Foxford')
@allure.story('Towers')
@pytest.mark.parametrize("n,start,finish,expected_result", test_data)
def test_move(n, start, finish, expected_result):
    print("| N ring | start | finish |")
    # assert expected_result == move(n, start, finish)
    move(n, start, finish)
