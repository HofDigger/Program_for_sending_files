import socket
import os

def open_file(path):
    with open(path, "rb") as file:
        return file.read()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8080))

while True:
    path = input("Enter the path to the file:")[1:-1]
    if not os.path.exists(path):
        print("File does not exist. Please try again.")
        continue

    file_to_send = open_file(path)
    name_to_send = os.path.basename(path)

    print(f"Trying to send {name_to_send}...")

    sock.sendall(name_to_send.encode())
    sock.sendall(path.encode())
    sock.sendall(file_to_send)
    sock.sendall(b"EOF")

    message_to_get = sock.recv(65536).decode()
    print(message_to_get)

    another_file = input("Do you want to send another file? (yes/no): ")
    if another_file.lower() != "yes":
        break

sock.close()
