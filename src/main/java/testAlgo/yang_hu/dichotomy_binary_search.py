from typing import List


def dichotomy_binary_search(input_array: List[int], search_value: int) -> List[int]:
    # TODO: implement this
    """
    wrong
    # if len(input_array) == 0:
    #     return -1
    if len(input_array)==1:
        if input_array[0]
    mid_index = len(input_array) // 2
    print(f"mid index = {mid_index}")
    if input_array[mid_index] == search_value:
        return mid_index
    if search_value < input_array[mid_index]:
        print(f"from {input_array[0]} to {input_array[mid_index]}")
        print(f"new input = {input_array[0:mid_index]}")
        return dichotomy_binary_search(input_array[0:mid_index], search_value)
    if search_value > input_array[mid_index]:
        print(f"from {input_array[mid_index+1]} to \
            1:len(input_array)-1]}")
        return dichotomy_binary_search(
            input_array[mid_index+1:len(input_array)-1], search_value)
    """
    # this works
    length = len(input_array)
    low = 0
    high = length - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] == search_value:
            return mid
        elif input_array[mid] < search_value:
            low = mid + 1
        elif input_array[mid] > search_value:
            high = mid - 1
    return -1
