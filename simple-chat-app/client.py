import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

nickname = input("Enter Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode("ascii"))


def handle():
    message = client.recv(1024).decode()
    print(message)


print("Connected Successfully!")

write_thread = threading.Thread(target=write)
handle_thread = threading.Thread(target=handle)
handle_thread.start()
while True:
    try:
        # Enter Nickname
        message = str(client.recv(1024).decode())
        if message == "NICKNAME":
            client.send(nickname.encode())
            write_thread.start()

    except:
        print("An error occured")
        client.close()
        break

    send_nickname = client.recv(1024).decode()
    client.send(input(send_nickname).encode())
