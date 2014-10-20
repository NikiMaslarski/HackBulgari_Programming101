def gcd(a, b):
    """
    Implementation of Stein's algorithm
    for finding Greatest Common Divisor
    """
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if ~a & 1:  # is a even
        if ~b & 1:  # is b even
            return gcd(a >> 1, b >> 1) << 1
        else:
            return gcd(a >> 1, b)

    if ~b & 1:  # a is odd, checks if b is even
        return gcd(a, b >> 1)

    if a > b:
        return gcd((a - b) >> 1, b)
    else:
        return gcd((b - a) >> 1, a)


def simplify_fraction(fraction):
    if fraction[1] == 0:
        raise Exception("Cannot devide by zero!!!")

    return (fraction[0] // gcd(*fraction),
            fraction[1] // gcd(*fraction))

