import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5555

clients = []
nicknames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print("Server is running")


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f"{client} left the chat!".encode('ascii'))
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def close():
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    print("Goodbye")


while True:
    try:
        client, address = server.accept()
        print(f"Connected: {address}")
        client.send("NICKNAME".encode())
        nickname = client.recv(1024).decode()
        print(f"ID: {address[1]} - NICKNAME: {nickname}")

        # Add client and nickname to list
        clients.append(client)
        nicknames.append(nickname)

        print("Connected Users")
        print(nicknames)

        # Broadcast newly connected user
        broadcast(f"{nickname} joined the chat!".encode())

        # Handle incoming messages
        handle_thread = threading.Thread(target=handle, args=(client,))
        handle_thread.start()

    except KeyboardInterrupt:
        sys.exit()
