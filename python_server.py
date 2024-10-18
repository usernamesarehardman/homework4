#!/usr/bin/env python3

import socket

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 12345

    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f"server started on {host}:{port}. Waiting for connection...")

    client_socket, addr = server_socket.accept()

    print(f"Got a connection from {addr}")

    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    client_socket.close()
    print("Connection closed.")

if __name__ == '__main__':
    start_server()