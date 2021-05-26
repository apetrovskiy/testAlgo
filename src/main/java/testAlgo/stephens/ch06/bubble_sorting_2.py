from typing import List


def bubble_sorting(input_array: List[int]) -> List[int]:
    not_sorted: bool = True
    while not_sorted:
        not_sorted = False
        for i in range(1, len(input_array)):
            if input_array[i] < input_array[i-1]:
                input_array[i], input_array[i - 1] = \
                    input_array[i-1], input_array[i]
                not_sorted = True
    return input_array
