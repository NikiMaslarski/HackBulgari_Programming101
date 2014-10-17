from employee import Employee


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def weeklyPay(self, hours):
        return self.salary

