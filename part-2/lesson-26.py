class A:

    def set_values(self):
        self.x = 1
        self.y = 2


a = A()
a.set_values()

b = A()

print(a.__dict__)
print(b.__dict__)
