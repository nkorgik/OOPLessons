class Person:

    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


p1 = Person(15, 'Trevor')
p2 = Person(22, 'Liza')

print(p1.name, p2.name)
print(p1.age, p2.age)

class Triangle:

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def check_equals(self):
        return self.a == self.b or self.b == self.c or self.a == self.c


t = Triangle(1, 23, 23.1)
print('Равнобедренный' if t.check_equals() else 'Неравнобедренный')
