class Employee():

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first, self.last, self.pay = first, last, pay
        self.email = self.first + '.' + self.last + '@company.com'

    def __repr__(self):
        # Un-amigeous representation of object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # Readable representation of object.
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Ganesh', 'Manal', 500000)
emp2 = Employee('Priyanaka', 'Manal', 200000)
print(emp1)

print(repr(emp1))
print(str(emp1))
print(len(emp1))
print('_'*60)

# Demo - Special Method - __add__
print("Combine Pay: {}".format(emp1+emp2))
print('_'*60)

# Special Methods
# int.__add__, str.__add__
print(1+2)
print('a'+'b')
print('_'*60)

# __len__
print(len('test'))
print('test'.__len__())
print('_'*60)
