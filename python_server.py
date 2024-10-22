#!/usr/bin/env python3

import socket

def start_server():
    try:
        # Create a socket object using IPv4 and TCP
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to all network interfaces on port 12345
        host = '0.0.0.0'
        port = 12345

        # Bind and listen for incoming connections
        server.bind((host, port))
        server.listen(2)

        print(f"Server started on {host}:{port}. Waiting for connections...")

        # Accept connections
        client, addr = server.accept()
        print(f"Connection from {addr}")

        while True:
            data = client.recv(1024).decode()
            if not data:
                break
            print(f"Received from client: {data}")
            data = input(' -> ')
            client.send(data.encode())

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client.close()
        server.close()

if __name__ == '__main__':
    start_server()
