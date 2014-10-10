def is_decreasing(seq):
    for index in range(len(seq) - 1):
        if seq[index] <= seq[index + 1]:
            return False
    return True

