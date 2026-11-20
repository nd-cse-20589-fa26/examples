#!/usr/bin/env python3

import dbm
import json
import sys

from vial import Vial

# Constants

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    print(f'Usage: {sys.argv[0]} HOST PORT', file=sys.stderr)
    sys.exit(1)

# Classes

class Database0:
    ''' Database 0: Only stored in memory '''

    def __init__(self):
        self.rooms = {}

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        return self.rooms.get(room, [])

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        try:
            self.rooms[room].append(message)
        except KeyError:
            self.rooms[room] = [message]

    def count(self, room: str) -> int:
        return len(self.rooms.get(room, []))

class Database1:
    ''' Database 1: Stored in multiple files (one per room) '''

    def __init__(self, prefix='doornote'):
        self.prefix = prefix

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        path = f'{self.prefix}.{room}'
        try:
            with open(path) as stream:
                return [line.strip() for line in stream]
        except OSError:
            return []

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        path = f'{self.prefix}.{room}'
        with open(path, 'a') as stream:
            stream.write(f'{message}\n')

    def count(self, room: str) -> int:
        path = f'{self.prefix}.{room}'
        with open(path) as stream:
            return sum(1 for _ in stream)

class Database2:
    ''' Database 2: Stored in a single JSON file '''

    def __init__(self, path='doornote.json'):
        self.path = path
        self.load()

    def load(self):
        try:
            with open(self.path) as stream:
                self.rooms = json.load(stream)
        except OSError:
            self.rooms = {}

    def save(self):
        with open(self.path, 'w') as stream:
            json.dump(self.rooms, stream)

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        return self.rooms.get(room, [])

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        try:
            self.rooms[room].append(message)
        except KeyError:
            self.rooms[room] = [message]

        self.save()

    def count(self, room: str) -> int:
        return len(self.rooms.get(room, []))

# Globals

App = Vial(HOST, PORT, {'db': Database1()})

# Handlers

@App.route('/room/([a-z]+-[0-9]{3})')
def doornote_messages(request, room: str) -> str:
    messages = App.db.messages(room)
    return ''.join(f'{i:04d}. {m}\n' for i, m in enumerate(messages))

@App.route('/room/([a-z]+-[0-9]{3})', methods=['POST'])
def doornote_append(request, room: str) -> str:
    App.db.append(room, request.post_data.decode())
    return f'{room} now has {App.db.count(room)} messages.\n'

# Main Execution

if __name__ == '__main__':
    App.run()
