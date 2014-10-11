def nth_fibonacci(n):
    current = 1
    previous = 1
    for i in range(2, n):
        current, previous = current + previous, current
    return current

