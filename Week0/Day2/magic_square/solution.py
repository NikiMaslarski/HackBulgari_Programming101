def magic_square(matrix):
    """
    Checks where the numbers in each row, and in each column,
    and the numbers in the forward and backward main diagonals,
    all add up to the same number.
    """

    temp_sum = sum(matrix[0])

    for row in matrix:
        if temp_sum != sum(row):
            return False

    for i in range(len(matrix)):
        sum_of_columns = 0
        for j in range(len(matrix)):
            sum_of_columns += matrix[j][i]

        if sum_of_columns != temp_sum:
            return False

    sum_of_main_diagonal = 0
    sum_of_backward_diagonal = 0
    for i in range(len(matrix)):
        sum_of_main_diagonal += matrix[i][i]
        sum_of_backward_diagonal += matrix[-1 - i][-1 - i]

    if sum_of_main_diagonal != temp_sum and \
       sum_of_backward_diagonal != temp_sum:
        return False

    return True

