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


def prime_factorization(n):
    prime = 2
    result = []
    current_number = 1

    while current_number <= n:
        if n % prime == 0:
            power = 0
            while n % prime == 0:
                n = n // prime
                power += 1
            result.append((prime, power))
            current_number *= pow(prime, power)
        prime = next_prime(prime)
    return result

