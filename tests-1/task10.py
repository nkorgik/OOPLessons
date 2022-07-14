# from pprint import pprint

results = []

class Auto:
    color: str = 'black'
    engine: str = '1.6'


with open('data') as file:
    arr = [car[:-1] for car in file.readlines()]


for index in range(len(arr)):
    car = arr[index].split()
    if car[2] == Auto.engine and car[3] == Auto.color:
        liked_car = Auto()
        liked_car.model = car[0] + ' ' + car[1]
        results.append(liked_car)
        print(liked_car.model)

print(results)
