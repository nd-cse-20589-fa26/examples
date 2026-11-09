#!/usr/bin/env python3

import sys

from vial import Vial

# Constants

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    print(f'Usage: {sys.argv[0]} HOST PORT', file=sys.stderr)
    sys.exit(1)

# Globals

App = Vial(HOST, PORT, {'greeting': 'Hello', 'default_name': 'Unknown'})

# Handlers

@App.route('/greeting')
def greet(request):
    name = request.query_data.get('name', App.default_name)
    return f'{App.greeting}, {name}!'

@App.route('/greeting', methods=['POST', 'PUT'])
def update(request):
    App.greeting     = request.form_data.get('greeting', App.greeting)
    App.default_name = request.form_data.get('name', App.default_name)
    return {'greeting': App.greeting, 'default_name': App.default_name}

# Main Execution

if __name__ == '__main__':
    App.run()
