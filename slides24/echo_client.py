#!/usr/bin/env python3

import socket
import sys

# Constants

BUFSIZ = (1<<10)

# Parse command line arguments

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    print('Usage: echo_client.py host port', file=sys.stderr)
    sys.exit(1)

# Connect to remote machine at host and port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))
    print(f'Connected to {host}:{port}')

    # Read from stdin, send to server, display response from server

    for line in sys.stdin:
        client.send(line.encode())
        response = client.recv(BUFSIZ)
        print(response.decode(), end='')
