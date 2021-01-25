from collections import Counter
from typing import List


def version01_clean_python(input: str) -> List[List[str]]:
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


def anagrams(input: str) -> List[str]:
    return version01_clean_python(input)
