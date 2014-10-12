def check_for_digits(set_of_digits):
    """
    Checks if set contains all digits from 1 to 9
    """
    for i in range(1, 10):
        if i not in set_of_digits:
            return False
    return True


def sudoku_solved(sudoku):
    for row in sudoku:
        if not check_for_digits(set(row)):
            return False

    for i in range(len(sudoku)):
        column = set()
        for j in range(len(sudoku)):
            column.add(sudoku[j][i])
        if not check_for_digits(column):
            return False

    # The middles of the squares in sudoku are all pairs of integers
    # obtained by permuting the numbers 1, 4 and 7
    midles_of_squares = (1, 4, 7)
    for index1 in midles_of_squares:
        for index2 in midles_of_squares:
            square = set()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    square.add(sudoku[index1 - i][index2 - j])
            if not check_for_digits(square):
                return False

    return True

