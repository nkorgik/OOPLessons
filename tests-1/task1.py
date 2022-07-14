class Cat:
    age: int = 2
    breed: str = 'Bengal'


tom = Cat()
setattr(tom, 'age', 1)
print(getattr(Cat, 'breed'), getattr(Cat, 'age'), sep='\n')
print()
print(tom.__dict__, tom.age)
