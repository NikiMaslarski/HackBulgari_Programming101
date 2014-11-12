import sqlite3


class ManageCompany:

    def __init__(self):
        self.conn = sqlite3.connect('firm.db')
        self.cursor = self.conn.cursor()

    def list_employees(self):
        self.cursor.execute('''SELECT id, name, position FROM employees''')
        for employee_id, name, position in self.cursor:
            print("{} - {} - {}".format(employee_id, name, position))

    def monthly_spending(self):
        self.cursor.execute('''SELECT monthly_salary, yearly_bonus
                            FROM employees''')
        year_spending = 0
        for salary, bonus in self.cursor:
            year_spending += salary + bonus / 12
        return year_spending

    def yearly_spending(self):
        self.cursor.execute('''SELECT monthly_salary, yearly_bonus
                            FROM employees''')
        year_spending = 0
        for salary, bonus in self.cursor:
            year_spending += salary * 12 + bonus
        return year_spending

    def __input_user_information(self):
        name = input("Employee Name: ")
        monthly_salary = input("Month salary: ")
        yearly_bonus = input("Yearly bonus: ")
        position = input("Employee position: ")
        return (name, monthly_salary, yearly_bonus, position)

    def add_employee(self):
        employee_information = self.__input_user_information()
        self.cursor.execute('''INSERT INTO employees(
            name,
            monthly_salary,
            yearly_bonus,
            position) VALUES(?, ?, ?, ?)''',
                            (employee_information[0], employee_information[1],
                             employee_information[2], employee_information[3]))
        self.conn.commit()

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM employees WHERE id=?",
                            (employee_id, ))

    def update_employee(self, employee_id):
        employee_information = self.__input_user_information()
        self.cursor.execute('''UPDATE employees SET
                            name=?,
                            monthly_spending=?,
                            yearly_bonus=?,
                            position=?
                            WHERE id=?''', (
                            employee_information[0],
                            employee_information[1],
                            employee_information[2],
                            employee_information[3],
                            employee_id))
