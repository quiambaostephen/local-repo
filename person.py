class Person:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

    def introduce_self(self):
        print('Hi my name is ' + self.name + ' and I am ' + self.personality)


p1 = Person('John Doe', 'Aggressive')
p1.introduce_self()
