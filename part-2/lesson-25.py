import operator

class Message:

    def calc_sum(instance, num_1: int, num_2):
        print(operator.add(num_1, num_2))


m = Message()
m.calc_sum(1, 2)
