import random
from pprint import pprint
from random import randrange

class Boy:
    age: int = 15
    height: int = 160


arr = [Boy() for _ in range(5)]
index = randrange(0, 5)
arr[index].height = 165
print(arr[index].__dict__)
arr_height = [arr[index].height for index in range(5)]
pprint(arr_height)

boy = random.choice(arr)
print(boy)
del boy
pprint(boy)
