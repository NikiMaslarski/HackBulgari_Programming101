def is_prime(n):
    for number in range(2, n // 2 + 1):
        if n % number == 0:
            return False
    return True

