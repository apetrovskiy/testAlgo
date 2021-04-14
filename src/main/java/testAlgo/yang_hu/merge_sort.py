from typing import List


def combine(array1: List[int], array2: List[int]) -> List[int]:
    result_array: List[int] = []
    i = 0
    j = 0
    while i < len(array1):
        while j < len(array2):
            print(f"array1 = {array1}")
            print(f"i = {i}")
            print(f"array1[{i}] = {array1[i]}")
            print(f"array2 = {array2}")
            print(f"j = {j}")
            print(f"array2[{j}] = {array2[j]}")
            if array1[i] < array2[j]:
                result_array.append(array1[i])
                print(f"result array = {result_array}")
                # i = i+1
                print("break!")
                break
            else:
                result_array.append(array2[j])
                print(f"result array = {result_array}")
                j = j+1
            # result_array.append(array1[i] if array1[i]
            #                     < array2[j] else array2[j])
            # j = j + 1
        # result_array.append(array1[i])
        print("after break")
        print(f"almost final i = {i}")
        print(f"almost final j = {j}")
        # if len(result_array)<len(array1)+len(array2):
        # print("less!")
        i = i + 1
    return result_array


def merge_sort(input_array: List[int]) -> List[int]:
    if len(input_array) < 2:
        return [input_array, ]
    if len(input_array) == 2:
        print("rearranging")
        return input_array if input_array[0] < \
            input_array[1] else [input_array[1], input_array[0]]
    half = len(input_array)//2
    print(f"half = {half}")
    print(f"array1 = {input_array[0:half]}")
    print(f"array2 = {input_array[half:len(input_array)]}")
    array1 = merge_sort(input_array[0:half])
    array2 = merge_sort(input_array[half:len(input_array)])
    # array1.extend(array2)
    return combine(array1, array2)
