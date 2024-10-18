#!/usr/bin/env python3

import socket

def start_server():

    # What does this do?
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the hostname
    host = socket.gethostname()
    port = 12345 # Initialize port number, must be higher than 1024

    # What does this do?
    server.bind((host, port))

    # What does this do?
    server.listen(2)

    print(f"server started on {host}:{port}. Waiting for connection...")

    client, addr = server.accept() # Accept new connection

    print(f"Connection from {addr}")

    while True:
        
        # Receive data stream, exclude packets greater than 1024 bytes
        data = client.recv(1024).decode() # What does utf-8 mean?

        if not data:

            # If data is not received then break
            break
    
        print(f"Received from client: {data}")
        data = input(' -> ')
        client(data.encode()) # Send data to client

    # Close the connection once operation is finished
    client.close()
    print("Connection closed.")

if __name__ == '__main__':
    start_server()