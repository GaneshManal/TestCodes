class Employee():

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first, self.last, self.pay = first, last, pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first, last, pay, prog_language):
        Employee.__init__(self, first, last, pay)
        self.prog_language = prog_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print emp.fullname()

dev_1 = Developer('Tom', 'Cruize', 1000, 'Python')
dev_2 = Developer('Chris', 'Bale', 1000, 'Java')
print(dev_1.email)
print(dev_1.prog_language)

mgr_1 = Manager('Sue', 'Smith', 2000, [dev_1])
print(mgr_1.email)
print(mgr_1.fullname())

print("-"*50)
mgr_1.add_employee(dev_2)
mgr_1.print_employees()

print("-"*50)
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print("-"*50)
print(issubclass(Developer, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
