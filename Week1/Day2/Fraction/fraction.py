from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        _gcd = gcd(numerator, denominator)
        self.__fraction = (numerator // _gcd, denominator // _gcd)

    def __eq__(self, other):
        return self.__fraction[0] == other.__fraction[0] and \
            self.__fraction[1] == other.__fraction[1]

    def __add__(self, other):
        return Fraction(self.__fraction[0] * other.__fraction[1] + other.__fraction[0]
                        * self.__fraction[1], self.__fraction[1] * other.__fraction[1])

    def __sub__(self, other):
        return Fraction(self.__fraction[0] * other.__fraction[1] - other.__fraction[0]
                        * self.__fraction[1], self.__fraction[1] * other.__fraction[1])

    def __lt__(self, other):
        if self.__fraction[0] * other.__fraction[1] < \
           other.__fraction[0] * self.__fraction[1]:
            return True
        return False

    def __qt__(self, other):
        if self.__fraction[0] * other.__fraction[1] < \
           other.__fraction[0] * self.__fraction[1]:
            return True
        return False

    def __str__(self):
        return "{} / {}".format(self.__fraction[0], self.__fraction[1])

