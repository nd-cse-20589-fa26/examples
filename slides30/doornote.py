#!/usr/bin/env python3

import json
import sqlite3
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

class Database:
    ''' Database: Stored in SQLite'''

    SQL_CREATE_MESSAGES = '''
    CREATE TABLE IF NOT EXISTS Messages(
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        room        TEXT NOT NULL,
        message     TEXT NOT NULL
    )
    '''

    SQL_INSERT_ROOM_MESSAGE  = 'INSERT INTO Messages(room, message) VALUES (?, ?)'
    SQL_SELECT_ROOM_MESSAGES = 'SELECT message FROM Messages WHERE room=?'
    SQL_SELECT_ROOM_COUNT    = 'SELECT Count(*) FROM Messages WHERE room=?'

    def __init__(self, path='doornote.db'):
        self.path = path
        self.conn = sqlite3.connect(self.path)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(self.SQL_CREATE_MESSAGES)

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(self.SQL_SELECT_ROOM_MESSAGES, (room,))
            return [row[0] for row in cursor.fetchall()]

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(self.SQL_INSERT_ROOM_MESSAGE, (room, message))

    def count(self, room: str) -> int:
        ''' Return number of messages for room. '''
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(self.SQL_SELECT_ROOM_COUNT, (room,))
            return cursor.fetchone()[0]

# Globals

App = Vial(HOST, PORT, {'db': Database()})

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
