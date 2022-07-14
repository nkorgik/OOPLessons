class A:
    pass


class B:
    pass


a, b = A(), B()

print(isinstance(a, B), type(b) == A, sep='\n')
# print(type(b) == B)
