from typing import List


def insertion_sort(input_array: List[int]) -> List[int]:
    for i in range(1, len(input_array)):
        for j in range(i, 0, -1):
            if input_array[j] < input_array[j-1]:
                input_array[j], input_array[j-1] = \
                    input_array[j-1], input_array[j]
            else:
                break
    return input_array
