def zero_insert(n):
    digits = []
    while n:
        digits.append(n % 10)
        n = n // 10
    digits.reverse()
    for index in range(len(digits) - 1):
        n *= 10
        n += digits[index]
        if digits[index] == digits[index + 1]:
            n *= 10
        elif (digits[index] + digits[index + 1]) % 10 == 0:
            n *= 10
    n = n * 10 + digits[-1]
    return n

