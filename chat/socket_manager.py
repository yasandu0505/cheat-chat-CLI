import socket

class ClientSocket:
    def __init__(self, host='127.0.0.1', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send(self, message):
        self.client.send(message.encode('utf-8'))

    def receive(self):
        return self.client.recv(1024).decode('utf-8')

    def close(self):
        self.client.close()
