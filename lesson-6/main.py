class Person:
    age = 18
    height = 175


person_1 = Person()
person_2 = Person()

person_1.hair_color = 'black'
person_2.hair_color = 'white'
person_1.height = 165

# print(person_1.__dict__, person_2.__dict__, Person.__dict__, sep='\n')

person_1.x = 'sdfhjsfd'
# print(Person.x) - мы не имеем права обращаться к атрибуту экземпляра класса через данный класс, забыл указать