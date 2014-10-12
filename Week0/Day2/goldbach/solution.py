def is_prime(n):
    for number in range(2, n // 2 + 1):
        if n % number == 0:
            return False
    return True


def next_prime(n):
    n = n + 1
    while not is_prime(n):
        n += 1
    return n


def goldbach(n):
    """
    returns a list of tupples,
    that is the goldbach conjecture
    for the given number n
    """
    prime1 = 2
    result = []
    while prime1 <= n // 2:
        prime2 = 2
        while prime2 < n:
            if prime1 + prime2 == n:
                result.append((prime1, prime2))
            prime2 = next_prime(prime2)
        prime1 = next_prime(prime1)
    return result

