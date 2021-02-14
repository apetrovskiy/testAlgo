import itertools
from collections import Counter
from typing import List


def version01_clean_python_mine(input: str) -> List[List[str]]:
    input_list = input.split(' ')
    print(input_list)
    l = [(x, ''.join(sorted(x))) for x in input_list]
    print(l)
    dict1 = dict(l)
    print(dict1)
    c = Counter(l)
    print(c)
    l2 = [(''.join(sorted(x)), x) for x in input_list]
    print(l2)
    dict2 = dict(l2)
    print(dict2)
    return []


def version02_clean_python_kite(input: str) -> List[List[str]]:
    input_list = input.split(' ')
    # https://www.kite.com/python/answers/how-to-group-a-list-by-values-in-python
    list_of_lists = [[x, ''.join(sorted(x))] for x in input_list]
    all_values = [list[1] for list in list_of_lists]
    unique_values = set(all_values)

    group_list = []
    for value in unique_values:
        this_group = []
        for list in list_of_lists:
            if list[1] == value:
                this_group.append(list[0])
        group_list.append(this_group)
    reduced_grouped_list = [
        x for x in group_list if len(x) > 1 and x[0] != x[1]]

    return reduced_grouped_list


def version03_itertools_kite(input: str) -> List[List[str]]:
    input_list = input.split(' ')
    # https://www.kite.com/python/examples/4677/itertools-group-list-items-by-keys
    list_of_lists = [[x, ''.join(sorted(x))] for x in input_list]
    def key_func(x): return x[0]

    print(list_of_lists)

    group_list = []
    for key, group in itertools.groupby(list_of_lists, key=key_func):
        group_list.append(list(group))

    print(group_list)

    reduced_grouped_list = [
        x for x in group_list if len(x) > 1 and x[0] != x[1]]
    return reduced_grouped_list


def anagrams(input: str) -> List[str]:
    # return version01_clean_python_mine(input)
    return version02_clean_python_kite(input)
    # return version03_itertools_kite(input)
