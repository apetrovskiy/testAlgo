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


def longest_math_sequence(s: str):
    max_length = 0
    current_length = 0
    previous_char = "."
    is_number = False
    for current_char in s:
        if current_char in "789" and previous_char in "-*.":
            is_number = True
        elif current_char in "-*":
            is_number = False
        elif current_char == "0" and previous_char in "-*.":
            is_number = False
        elif current_char in "0789" and previous_char in "789":
            is_number = True
        if current_char in "0789" and previous_char == "0":
            if is_number:
                current_length += 1
            else:
                max_length = (
                    current_length if current_length > max_length else max_length
                )
                current_length = 1
        elif current_char in "-*" and previous_char in "-*":
            max_length = (
                current_length - 1 if current_length > max_length else max_length
            )
            current_length = 0
        else:
            current_length += 1
        previous_char = current_char
    if s[-1:] in "-*":
        current_length -= 1
    max_length = current_length if current_length > max_length else max_length
    return max_length
