"""Существует некоторый класс Computer, со следующими атрибутами -
age
price
size : str = ‘big’
Сделайте таким образом, чтобы программа выводила число pi при попытке обращения к атрибуту - sdf. Выведите mappingproxy класса, используя pprint.
Удалите один из атрибутов данного класса, используя инструкцию del, другой при помощи - delattr.
"""
import pprint
import math

class Computer:
    age: int = 5
    price: int = 200
    size: str = 'big'


print(getattr(Computer, 'sdf', str(math.pi)))
pprint.pprint(Computer.__dict__)
del Computer.price
delattr(Computer, 'size')

print(Computer.__dict__)
