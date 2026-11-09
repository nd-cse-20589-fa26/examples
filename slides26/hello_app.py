#!/usr/bin/env python3

import sys

from functools import cached_property
from http.client import responses
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse

# Classes

class HelloRequestHandler(BaseHTTPRequestHandler):

    greeting: str='Hello'

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

        name = self.query_data.get('name', 'Unkown')
        self.wfile.write(f'{self.greeting}, {name}'.encode())

    def do_POST(self):
        if not (greeting := self.form_data.get('greeting')):
            self.send_response(400)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        HelloRequestHandler.greeting = greeting
        self.wfile.write(f'Greeting is {HelloRequestHandler.greeting}'.encode())

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
