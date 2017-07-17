class Employee:

    # Maintain number of employees.
    num_of_employees = 0

    # Class  variables shares the same copy for all the instances.
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first, self.last, self.pay = first, last, pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Tom', 'Cruise', 200)
emp_2 = Employee('Christian', 'Bale', 100)
print('Employee Count: {}'.format(Employee.num_of_employees))

print(Employee.raise_amount)
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

'''
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
'''

'''
# Printing
print(emp_1.fullname())
print(emp_2.fullname())

# Instance method can be called this way as well.
print(Employee.fullname(emp_1))
'''
