from typing import List


def swap(input_array: List[int], index: int):
    if index < len(input_array)-1 and \
            input_array[index] > input_array[index+1]:
        input_array[index], input_array[index + 1] = \
            input_array[index+1], input_array[index]


def bubble_sort(input_array: List[int]) -> List[int]:
    [[swap(input_array, index) for index in range(already_sorted_index)]
     for already_sorted_index in range(len(input_array), 1, -1)]
    return input_array
