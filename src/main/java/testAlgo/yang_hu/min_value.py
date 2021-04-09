from typing import List


def min_value(input_array: List[int]) -> int:
    min_index = 0
    for i in range(1, len(input_array)):
        if input_array[min_index] > input_array[i]:
            min_index = i
    return input_array[min_index]
