def is_prime_number(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
