import pprint

class Person:
    name: str = 'MAx'
    age: int = 37


setattr(Person, 'hair_color', 'black')
pprint.pprint(Person.__dict__)

print(getattr(Person, 'hair_color', 'No'))

delattr(Person, 'hair_color')

pprint.pprint(Person.__dict__)
