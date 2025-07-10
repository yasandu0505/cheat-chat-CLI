def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message, client_socket, clients)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)
