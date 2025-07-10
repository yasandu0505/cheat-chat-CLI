import socket
from chat.chat_server import handle_client
from threading import Thread


HOST = '0.0.0.0'
PORT = 12345
clients = []

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"🔌 Server started on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"✅ New connection from {addr}")
        clients.append(client_socket)
        thread = Thread(target=handle_client, args=(client_socket, clients))
        thread.start()