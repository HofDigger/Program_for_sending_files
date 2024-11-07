import socket
import os
import ssl

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(1)

while True:
    con, addr = sock.accept()
    ssl_con = ssl.wrap_socket(con, server_side=True, certfile="server.crt", keyfile="server.key")
    print(f"Connection from {addr}")

    while True:
        file_name = ssl_con.recv(65536).decode()
        if not file_name:
            break

        with open(f"C:\\Users\\illia\\Desktop\\Files\\{file_name}", "wb") as file1:
            while True:
                file_data = ssl_con.recv(1024)
                if file_data == b"EOF":
                    break
                if not file_data:
                    break
                file1.write(file_data)

        ssl_con.sendall("File has been downloaded successfully!".encode())

    ssl_con.close()
