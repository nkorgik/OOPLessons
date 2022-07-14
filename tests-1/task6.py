# class A:
#     x: int = 15
#
#
# a = A()
# a.y = 'hello'
# print(A.__dict__, a.__dict__, sep='\n')
# setattr(A, 'x', 12478)
# print(A.x)
import math

class Circle:
    radius: float = 5.0


class Rectangle:
    width: float = 5.
    height: float = 7.


print(math.pi*Circle.radius**2)
print()
print(Rectangle.width*Rectangle.height)
# print(operator.mul(Rectangle.width, Rectangle.height))

