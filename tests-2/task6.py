"""Создайте класс, объявите внутри него пустую функцию.
Динамически подключите к классу новый атрибут со значением 5.
Проверьте, является ли данный атрибут - свойством конкретного экземпляра данного класса.
Обратитесь к данной функции и выведите результат обращения.
"""

class A:

    def send():
        pass


A.attr = 5
a = A()
print(a.attr in a.__dict__)
print(A.send)