def is_int_palindrome(n):
    digits_of_n = [digit for digit in str(n)]
    for i in range(1, len(digits_of_n) + 1):
        if digits_of_n[i - 1] != digits_of_n[-i]:
            return False
    return True


def is_hack(n):
    binary_n = bin(n)[2:]
    if binary_n.count('1') % 2:
        if is_int_palindrome(int(binary_n)):
            return True
    return False


def next_hack(n):
    while True:
        n += 1
        if is_hack(n):
            return n

