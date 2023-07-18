from typing import List


def insertion_sort(input_array: List[int]) -> List[int]:
    for i in range(1, len(input_array)):
        j = i - 1
        element_next = input_array[i]
        while input_array[j] > element_next and j >= 0:
            input_array[j + 1] = input_array[j]
            j = j - 1
        input_array[j + 1] = element_next
    return input_array
