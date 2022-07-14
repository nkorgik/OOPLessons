# class Message:
#
#     def send_hello():
#         return 'Hello'
#
#     def send_world():
#         return 'World!'
#
#
# print(Message.send_hello() + ' ' + getattr(Message, 'send_world')())
#

class A:

    def factorial(n):
        if n==0 or n==1:
            return 1
        return A.factorial(n-1)


print(A.factorial(5))