class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0,
                      10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for value, price in money.items():
            self.money[value] += price

    def total(self):
        total_money = 0
        for key in self.money:
            total_money += self.money[key] * key
        return total_money

    def can_withdraw_money(self, amount_of_money):
        if self.total() < amount_of_money:
            return False

