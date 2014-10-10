def sum_matrix(m):
    sum_ = 0
    for column in m:
        for element in column:
            sum_ += element
    return sum_

