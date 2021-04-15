from typing import List


def bubble_sort(input_array: List[int]) -> List[int]:
    last_element_index = len(input_array)-1
    for pass_no in range(last_element_index, 0, -1):
        for index in range(pass_no):
            if input_array[index] > input_array[index+1]:
                input_array[index], input_array[index + 1] = \
                    input_array[index+1], input_array[index]
    return input_array
