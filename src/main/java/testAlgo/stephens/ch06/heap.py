from typing import List


def array_to_heap_stephens(input_array: List[int]) -> List[int]:
    """A non-working array to max heap implementation by Rod Stephens"""
    for i in range(len(input_array)):
        index: int = i
        while index != 0:
            parent_index: int = (index - 1) // 2
            if input_array[index] <= input_array[parent_index]:
                break
            input_array[index], input_array[parent_index] = input_array[parent_index], input_array[index]
            # temp: int = input_array[index]
            # input_array[index] = input_array[parent_index]
            # input_array[parent_index] = temp
            index = parent_index
    print(input_array)
    return input_array


def heapify(input_array: List[int], array_len: int, current_index: int):
    largest: int = current_index
    left_child_index = 2*current_index+1
    right_child_index = 2*current_index+2
    if left_child_index < array_len and input_array[left_child_index] > input_array[largest]:
        largest = left_child_index
    if right_child_index < array_len and input_array[right_child_index] > input_array[largest]:
        largest = right_child_index

    if largest != current_index:
        input_array[current_index], input_array[largest] = input_array[largest], input_array[current_index]
        heapify(input_array, array_len, largest)


def array_to_heap(input_array: List[int]) -> List[int]:
    """An array to max heap implementation by GfG"""
    start_index = len(input_array) // 2 - 1
    array_len = len(input_array)
    for i in range(start_index, -1, -1):
        heapify(input_array, array_len, i)
    print(input_array)
    return input_array
