# class A:
#     x: float = 17.8
#
#
# A.y = 'sfdjksdf'
# print(A.x)
# del A.x
# print(A.__dict__)

# class B:
#     x: int = 15
#     y: int = 7
#
#
# print(getattr(B, 'x') + getattr(B, 'y'))
# print(getattr(B, 'z', 'There\'s no such number'))

# class C:
#     pass
#
#
# setattr(C, 'x', 11)
# C.y = 'hello world'
# print(getattr(C, 'y').upper())
# print(C.__dict__)


# class D:
#     x: int = 14
#     y: float = 15.6
#
#
# del D.x
# print(getattr(D, 'x', 'impossible'))
# delattr(D, 'y')
# print(D.__dict__)