"""Что такое метод инициализации экземпляра?
Опишите его внутри произвольного класса, пусть при инициализации экземпляра,
будут создаваться два динамических атрибута, один из которых будет принимать значение “по умолчанию”.
"""
class A:

    def __init__(self, x: int) -> None:
        self.x: int = x
        self.y: str = 'default'


a = A(23)
print(a.__dict__)

