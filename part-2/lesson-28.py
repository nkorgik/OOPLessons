import operator


class A:

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def send_sum(self):
        return operator.add(self.x, self.y)  # a + b


a = A()
a.set_values(5, 2)
result = a.send_sum()

print(result)
