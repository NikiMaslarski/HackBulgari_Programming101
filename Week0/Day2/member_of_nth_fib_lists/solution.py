def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA

    previous = listA
    current = listB
    for i in range(2, n):
        current, previous = previous + current, current
    return current


def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    temp = nth_fib_lists(listA, listB, n)
    while len(needle) >= len(temp):

        if needle == temp:
            return True
        temp = nth_fib_lists(listA, listB, n)
        n += 1
    return False

