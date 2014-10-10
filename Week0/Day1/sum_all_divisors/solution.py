def get_all_divisors(n):
    divisors = [1]
    for number in range(2, n // 2 + 1):
        if n % number == 0:
            divisors.append(number)
    divisors.append(n)
    return divisors


def sum_of_divisors(n):
    result = 0
    divisors = get_all_divisors(n)
    for divisor in divisors:
        result += divisor
    return result

