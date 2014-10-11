from functools import cmp_to_key


def compare_fractions(fraction1, fraction2):
    '''
    Returns True if the first fraction
    is bigger than the second
    '''
    if fraction1[0] * fraction2[1] > fraction2[0] * fraction1[1]:
        return 1

    elif fraction1[0] * fraction2[1] < fraction2[0] * fraction1[1]:
        return -1

    else:
        return 0


def sort_fractions(fractions):
    return sorted(fractions, key=cmp_to_key(compare_fractions))

