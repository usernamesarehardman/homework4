#!/usr/bin/env python3

import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 12345

    client_socket.connect((host, port))

    message = "Hella from the client!"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    client_socket.close()

if __name__ == '__main__':
    start_client()