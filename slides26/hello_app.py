#!/usr/bin/env python3

import logging
import sys

from functools import cached_property
from http.client import responses
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse

# Classes

class HelloRequestHandler(BaseHTTPRequestHandler):

    default_name: str='Unknown'

    # Helper Properties from RealPython

    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers.get('Content-Length', 0))
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode('utf-8')))

    # Handle Error

    def error(self, status_code: int):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        self.wfile.write(responses[status_code].encode())

    # Handle HTTP Methods

    def do_GET(self):
        if self.url.path != '/':
            self.error(404)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        name = self.query_data.get('name', self.default_name)
        self.wfile.write(f'Hello, {name}'.encode())

    def do_POST(self):
        if not (name := self.form_data.get('name')):
            self.send_response(400)

        HelloRequestHandler.default_name = name

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Default name is {HelloRequestHandler.default_name}'.encode())

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    try:
        host = arguments[0]
        port = int(arguments[1])
    except IndexError:
        print('Usage: hello_app.py host port', file=sys.stderr)

    server = HTTPServer((host, port), HelloRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
