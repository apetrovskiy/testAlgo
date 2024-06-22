def longest_math_sequence_by_lanskaya(s: str):
    s = s.replace("-", "*")
    s = s.split("*")
    buf = ""
    ans = ""
    for x in s:
        if len(x) > 0 and x[0] != "0":
            buf += x + "*"
            ans = max(ans, buf, key=len)
        else:
            buf = ""
    return len(ans) - 1


# def longest_math_sequence(s: str):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[-1] and is_palindrome(s[1:-1])
