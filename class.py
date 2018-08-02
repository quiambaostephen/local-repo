class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('Hi I am ' + self.name)


r1 = Robot('John Doe', 'Blue', 24)
r1.introduce_self
