def contains_digit(number, digit):
    while number:
        if number % 10 == digit:
            return True
        number = number // 10
    return False

