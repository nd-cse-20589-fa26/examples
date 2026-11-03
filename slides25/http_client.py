#!/usr/bin/env python3

import socket
import ssl
import sys

from urllib.parse import urlsplit

# Parse command line arguments

try:
    url = urlsplit(sys.argv[1])
except IndexError:
    print('Usage: http_client.py URL', file=sys.stderr)
    sys.exit(1)

# Create socket (wrap with ssl if scheme is HTTPS)

socket = socket.create_connection((url.hostname, url.port))
if url.scheme == 'https':
    context = ssl.create_default_context()
    socket  = context.wrap_socket(socket, server_hostname=url.hostname)

with socket:
    # Send HTTP Request
    with socket.makefile('w', encoding='utf-8') as wfile:
        wfile.write(f'GET {url.path} HTTP/1.0\r\n')
        wfile.write(f'Host: {url.hostname}\r\n')
        wfile.write('\r\n')
    
    # Read HTTP Response
    with socket.makefile('r', encoding='utf-8') as rfile:
        while line := rfile.readline().strip():
            print(line)

        print()
        print(rfile.read())
