class Person:
    age = 18
    height = 175


a = Person()
b = Person()

# print(a.age, b.height)
a.x = 55  # динамически создаётся новый атрибут экземпляра класса Person
# print(a.x)
# print(Person.__dict__, a.__dict__, sep='\n')
a.age = 17
print(Person.age, a.__dict__)