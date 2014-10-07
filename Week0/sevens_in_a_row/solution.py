def sevens_in_a_row(arr, n):
    counter = 0
    for number in arr:
        if number == 7:
            counter += 1
            if counter == n:
                return True
        else:
            counter = 0
    return False
