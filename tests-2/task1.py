# OOP - methodology ? stage of OO development
# class ? - pattern | blueprint
# instance of the class
# states and behavior
class Cat:
    age: int = 2  # статические атрибуты / атрибуты класса / состояние класса / свойства класса**
    breed: str = 'Bengal'

    def __init__(self, color: str):  # конструктор класса / метод инициализации экземпляра | АТРИБУТ КЛАССА
        self.color: str = color  # динамический атрибут / локальные свойства / атрибут экземпляра / состояние объекта

    def meow(self) -> None:  # method instance
        print('MEOW')


tom = Cat('black')
# Cat.meow(tom)

getattr(Cat, 'meow')(tom)  # setattr, delattr, del

# print(tom.__dict__)

# print(Cat.__dict__)


