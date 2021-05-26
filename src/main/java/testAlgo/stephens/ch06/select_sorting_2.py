from typing import List


def select_sorting(input_array: List[int]) -> List[int]:
    for i in range(0, len(input_array)):
        for j in range(i, len(input_array)):
            if j > i and input_array[j] < input_array[i]:
                input_array[i], input_array[j] = input_array[j], input_array[i]
    return input_array
