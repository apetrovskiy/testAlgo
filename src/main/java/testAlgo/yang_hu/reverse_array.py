from typing import List


def swap(input_array: List[int], index: int):
    length = len(input_array)
    input_array[index], input_array[length - index - 1] = (
        input_array[length - index - 1],
        input_array[index],
    )


def reverse_array(input_array: List[int]) -> List[int]:
    half = len(input_array) // 2
    [swap(input_array, i) for i in range(half)]
    return input_array
