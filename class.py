class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Doe', 5000)
print(emp1)
print(emp1.fullName())
