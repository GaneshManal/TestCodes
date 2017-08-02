class Employee(object):

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first, self.last, self.pay = first, last, pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first, self.last = None, None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

'''
emp1 = Employee('Ganesh', 'Manal', 500000)
print(emp1)
print(emp1.first)
print(emp1.email)
print(emp1.fullname())\
'''

emp1 = Employee('xyz', 'abc', 10000)
emp1.fullname = 'Raj Kumar'
print(emp1.email)
print(emp1.first)
del emp1.fullname
print(emp1.email)