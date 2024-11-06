import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(1)

while True:
    con, addr = sock.accept()
    print(f"Connection from {addr}")

    while True:
        file_name = con.recv(65536).decode()
        if not file_name:
            break

        path = con.recv(65536).decode()

        with open(f"C:\\Users\\illia\\Desktop\\Files\\{file_name}", "wb") as file1:
            while True:
                file_data = con.recv(1024)
                if file_data == b"EOF":
                    break
                if not file_data:
                    break
                file1.write(file_data)

        con.sendall("File has been downloaded successfully!".encode())

    con.close()
