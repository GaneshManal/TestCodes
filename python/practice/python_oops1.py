import datetime


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

    # Use class methods as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() >= 5:
            return False
        return True

emp1_str = 'Tom-Cruise-200'
emp2_str = 'Christian-Bale-100'

# Initialize the object using parsing.
emp_1 = Employee.from_string(emp1_str)
print(emp_1.fullname())

# Monday
my_date = datetime.datetime(2017, 7, 17)
print(Employee.is_work_day(my_date))
