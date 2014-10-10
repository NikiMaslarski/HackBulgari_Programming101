def is_number_balanced(n):
    digits_in_n = [int(digit) for digit in str(n)]
    result = 0
    for i in range(1, len(digits_in_n) // 2 + 1):
        result += digits_in_n[i - 1]
        result -= digits_in_n[-i]
    return not result

