def factor(n: int) -> List[int]:
    ans = []
    for d in range(2, n + 1):
        if n % d == 0:
            ans.append(d)
    return ans
