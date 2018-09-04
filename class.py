class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)


 class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
           self.employees.remove(emp)

     def print_emps(self):
        for emp in self.employees:
            print('-->', self.fullname())


dev_1 = Developer('John', 'Doe', 5000, 'Python')
dev_2 = Developer('Jane', 'Doe', 6000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 9000, [dev1])

print(mgr_1.email)

mgr_1.add_emp(dev1)
mgr_1.remove_emp(dev1)

mgr_1.print_emps()

