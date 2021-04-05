from typing import List


def factor(n: int) -> List[int]:
    ans = []
    for d in range(2, n + 1):
        # version 01
        # if n % d == 0:
        #     ans.append(d)
        # if n % d == 0:
        #     while n % d == 0:
        #         ans.append(d)
        #         n //= d
        # version 03
        # while n % d == 0:
        #     ans.append(d)
        #     n //= d
        # version 04
        if n % d == 0:
            ans.append(d)
        while n % d == 0:
            n //= d
        # version 05
    return ans
