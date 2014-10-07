def contains_digits(number, digits):
    digits_in_number = [int(digit) for digit in str(number)]
    for digit in digits:
        if digit not in digits_in_number:
            return False
    return True

