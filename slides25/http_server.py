#!/usr/bin/env python3

import datetime
import socket
import sys

# Parse command line arguments

try:
    host = '127.0.0.1'
    port = int(sys.argv[1])
except IndexError:
    print('Usage: http_server.py port', file=sys.stderr)
    sys.exit(1)

# Create and advertise server socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Bind to port and begin listening
    server.bind((host, port))
    server.listen()
    print(f'Listening on {host}:{port}')

    while True:
        # Accept a client
        client, address = server.accept()

        with client:
            print(f'Accepted connection from {address[0]}:{address[1]}')

            # Read HTTP request
            with client.makefile('r', encoding='utf-8') as rfile:
                while line := rfile.readline().strip():
                    print(line)

            # Send HTTP response
            with client.makefile('w', encoding='utf-8') as wfile:
                wfile.write('HTTP/1.0 200 OK\r\n')
                wfile.write('Context-Type: text/plain\r\n')
                wfile.write('\r\n')
                wfile.write(str(datetime.datetime.now()))
