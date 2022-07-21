"""Реализуйте метод __init__ в классе окружностей.
Реализуйте метод вычисления площади данных окружностей.
"""
import math

class Circumference:

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calc_square(self) -> float:
        return math.pi * self.radius**2


c = Circumference(3.4)
print(c.calc_square())
