def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA

    previous = listA
    current = listB
    for i in range(2, n):
        current, previous = current + previous, current
    return current

