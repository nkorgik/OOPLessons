class Message:

    def send_hello():
        return 'Hello'

    def send_world():
        return 'World!'


print(Message.send_hello() + ' ' + getattr(Message, 'send_world')())
