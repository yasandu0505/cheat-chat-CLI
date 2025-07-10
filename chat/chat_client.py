import threading
from chat.socket_manager import ClientSocket

def receive_messages(socket_obj):
    while True:
        try:
            msg = socket_obj.receive()
            print(f"\n📨 {msg}\n")
        except:
            print("❌ Disconnected from server.")
            break

def start_client():
    socket_obj = ClientSocket()

    username = input("Enter your name: ").strip()
    print("✅ Connected to server. Start chatting! Type '/quit' to exit.")

    # Start thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(socket_obj,))
    thread.daemon = True
    thread.start()

    # Main input loop
    while True:
        msg = input()
        if msg.lower() == "/quit":
            socket_obj.close()
            break
        full_msg = f"{username}: {msg}"
        socket_obj.send(full_msg)
