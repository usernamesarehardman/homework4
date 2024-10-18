#!/usr/bin/env python3

import socket

def start_client():

    # What does this do?
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get host name, configured to run on same PC as host
    host = socket.gethostname()
    port = 12345 # Initialize port number, must be higher than 1024

    # Initiate connection
    client.connect((host, port))

    message = input(" -> ") # Message input

    while message.lower().strip() != 'bye':
        client.send(message.encode()) # Send message
        response = client.recv(1024).decode() # Receive message
        print(f"Received from server: {response}")

        # Recursive input
        message = input(" -> ")

    # Close the connection
    client.close()

if __name__ == '__main__':
    start_client()