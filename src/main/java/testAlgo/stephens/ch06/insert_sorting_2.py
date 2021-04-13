from typing import List


def insert_sorting(input_array: List[int]) -> List[int]:
    for i in range(0, len(input_array)):
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[i]:
                input_array[j], input_array[i] = input_array[i], input_array[j]
    return input_array
