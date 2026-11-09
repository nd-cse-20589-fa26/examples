#!/usr/bin/env python3

import json
import re

from functools import cached_property
from http.client import responses
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Callable
from urllib.parse import parse_qsl, urlparse

# Classes

class VialRequestHandler(BaseHTTPRequestHandler):

    Routes: dict[str, dict[str, Callable]] = {}

    # Utility properties from RealPython

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
        if self.headers.get('Content-Type') == 'application/json':
            return json.loads(self.post_data.decode('utf-8'))
        else:
            return dict(parse_qsl(self.post_data.decode('utf-8')))

    # Do HTTP Methods

    def do_METHOD(self, method: str):
        if not method in VialRequestHandler.Routes:
            return self.write_error(405)

        for pattern, callback in VialRequestHandler.Routes[method].items():
            if match := re.fullmatch(pattern, self.url.path):
                result = callback(self, *match.groups())
                match result:
                    case int():  return self.write_error(result)
                    case str():  response, *args = result, 200, 'text/plain'
                    case dict(): response, *args = json.dumps(result), 200, 'application/json'
                    case None:   response, *args = '', 200, 'text/plain'
                    case _:      response, *args = result
                return self.write_text(response, *args) # type: ignore[arg-type]

        return self.write_error(405)

    def do_DELETE(self):
        self.do_METHOD('DELETE')

    def do_GET(self):
        self.do_METHOD('GET')

    def do_PATCH(self):
        self.do_METHOD('PATCH')

    def do_POST(self):
        self.do_METHOD('POST')

    def do_PUT(self):
        self.do_METHOD('PUT')

    # Writers

    def write_text(self, text: str, status_code: int=200, mimetype: str='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-Type', mimetype)
        self.end_headers()
        self.wfile.write(text.encode())

    def write_error(self, status_code: int):
        self.write_text(responses[status_code], status_code=status_code)


class Vial(HTTPServer):
    def __init__(self, host: str='127.0.0.1', port: int=8080, attributes=None):
        super().__init__((host, port), VialRequestHandler)
        if attributes:
            for key, value in attributes.items():
                setattr(self, key, value)

    def route(self, pattern: str, methods: list[str]=['GET']):
        def decorator(callback):
            for method in methods:
                try:
                    VialRequestHandler.Routes[method].update({pattern: callback})
                except KeyError:
                    VialRequestHandler.Routes[method] = {pattern: callback}
            return callback
        return decorator

    def run(self):
        self.serve_forever()
