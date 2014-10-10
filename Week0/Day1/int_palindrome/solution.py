def is_int_palindrome(n):
    digits_of_n = [digit for digit in str(n)]
    for i in range(1, len(digits_of_n) + 1):
        if digits_of_n[i - 1] != digits_of_n[-i]:
            return False
    return True

