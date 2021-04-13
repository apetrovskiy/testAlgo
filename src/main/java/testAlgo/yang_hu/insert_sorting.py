from typing import List


def insert_sorting(input_array: List[int]) -> List[int]:
    '''
    for i in range(0, len(input_array)-1):
        insert_element = input_array[i]
        insert_position = i
        for j in range(insert_position-1, 1, -1):
            print(
                f"insert element = \
                    {insert_element} insert position = {i} j = {j}")

            if insert_element < input_array[j]:
                input_array[j+1] = input_array[j]
                insert_position = 1
        input_array[insert_position] = insert_element
    '''
    i = 1
    while i < len(input_array):
        j = i
        while j > 0 and input_array[j-1] > input_array[j]:
            input_array[j], input_array[j-1] = input_array[j-1], input_array[j]
            j = j - 1
        i = i + 1
    return input_array
