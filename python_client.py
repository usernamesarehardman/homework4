#!/usr/bin/env python3

import socket

def start_client():
    try:
        # Create a socket object using IPv4 and TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Use the server's IP address here (replace with actual server IP)
        host = '10.0.2.15' # Public IP: 156.110.185.130
        port = 12345

        # Connect to the server
        client.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        message = input(" -> ")
        while message.lower().strip() != 'bye':
            client.send(message.encode())
            response = client.recv(1024).decode()
            print(f"Received from server: {response}")
            message = input(" -> ")

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    start_client()
