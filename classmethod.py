"""classmethod()
@classmethod
factory
"""

class A:
    x = 5
    y = 2

    def __init__(self, a: float):
        self.a = a

    @classmethod
    def sub(cls):
        return cls(13)


print(A.sub().__dict__)
