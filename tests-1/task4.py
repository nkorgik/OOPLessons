class A:
    pass


A.state = 'example'
print(A.__dict__)
a = A()
print(isinstance(a, A))
print(a.__dict__)
