#!/usr/bin/env python3

import socket
import sys

# Constants

BUFSIZ = (1<<10)

# Parse command line arguments

try:
    host = '127.0.0.1'
    port = int(sys.argv[1])
except IndexError:
    print('Usage: echo_server.py port', file=sys.stderr)
    sys.exit(1)

# Connect to remote machine at host and port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Bind to port and begin listening
    server.bind((host, port))
    server.listen()
    print(f'Listening on {host}:{port}')

    while True:
        # Accept a client
        client, address = server.accept()

        with client:
            print(f'Accepted connection from {address}')

            # Read from client and send it back
            while request := client.recv(BUFSIZ):
                print(request.decode(), end='')
                client.send(request)
