from salaried_employee import SalariedEmployee


class Manager(SalariedEmployee):

    def __init__(self, name, salary, bonus):
        SalariedEmployee(self, name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary + self.bonus

