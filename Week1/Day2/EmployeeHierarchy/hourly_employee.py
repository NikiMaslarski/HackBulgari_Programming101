from employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def weeklyPay(self, hours):
        if hours > 40:
            return hours * self.salary * 1.5
        return hours * self.salary

