from typing import List


def max_value(input_array:List[int]):
    print(f"length = {len(input_array)}")
    for i in range(len(input_array)):
        print(i)
        if i<len(input_array)-2 and input_array[i]>input_array[i +1]:
            input_array[i],input_array[i+1]=input_array[i+1],input_array[i]
    return input_array[len(input_array)-1]