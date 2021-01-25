from random import randint


def is_prime(p: int, max_tests: int) -> bool:
    for test in range(1, max_tests + 1):
        if randint(2, p - 1) % p != 1:
        # if randint(1, p) % p != 1:
            return False
    return True
