# class Man:
#     height = 175
#     weight = 65
#     amount: int = 150
#     year: int = 2020
#
#
# Man.year += 1
# Man.amount -= 2
# print(Man.__dict__)
class Cat:
    color: str = 'white'
    amount = 14


arr = [Cat() for _ in range(14)]
arr[0].color = arr[1].color = 'black'
print(arr[0].__dict__, arr[1].color, arr[5].color)
