from random import random


class Weapon:

    def __init__(self, category, damage, critical_strike_percent):
        self.category = category
        self.damage = damage
        self.__set_critical_strike_percent(critical_strike_percent)

    def __set_critical_strike_percent(self, critical_strike_percent):
        if critical_strike_percent >= 0 and critical_strike_percent <= 1:
            self.critical_strike_percent = critical_strike_percent
        else:
            raise ValueError

    def critical_hit(self):
        seed = random()

        if seed < self.critical_strike_percent:
            return True

        return False

