import re


def iterations_of_nan_expand(expanded):
    if expanded:
        if not re.match(r'(Not a )+NaN$', expanded):
            return False
        return expanded.count("Not a ")
    return 0

