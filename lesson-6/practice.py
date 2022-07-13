class Person:
    age: int = 20
    height: int = 170


person_1 = Person()
person_2 = Person()

person_1.height = 160
print(person_1.__dict__)

person_2.hair_color = 'black'
print(person_2.__dict__)


print(Person.__dict__)

print(Person.hair_color)
