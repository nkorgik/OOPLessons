class Car:
    speed: float = 90.0
    color: str = 'red'


print(Car.speed, Car.color, sep='\n')
del Car.speed
print(Car.__dict__)
