from typing import List


def swap(input_array: List[int], i: int):
    if input_array[i] > input_array[i + 1]:
        input_array[i], input_array[i+1] = input_array[i+1], input_array[i]


def bubble_sorting(input_array: List[int]):
    [[swap(input_array, i) for i in range(0, max-1)]
     for max in range(len(input_array), 1, -1)]
    return input_array
