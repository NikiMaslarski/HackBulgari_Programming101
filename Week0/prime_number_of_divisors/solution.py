def is_prime(n):
    for number in range(2, n//2 +1):
        if n % number == 0:
            return False
    return True

def prime_number_of_divisors(n):
    count_of_divisors = 2;
    for number in range(2, n//2 + 1):
        if n % number == 0:
            count_of_divisors += 1
    return is_prime(count_of_divisors)

