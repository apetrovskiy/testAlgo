from typing import List


def select_sorting(input_array: List[int]) -> List[int]:
    # min_index = 0
    for i in range(len(input_array) - 1):
        for j in range(i+1, len(input_array)):
            if input_array[i] > input_array[j]:
                # min_index = j
                input_array[i], input_array[j] = input_array[j], input_array[i]
    return input_array
