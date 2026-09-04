#!/usr/bin/env python3

import csv
import os
import re
import sys

from typing import Optional

# Constants

PS_COMMAND = 'ps -e -o pid,user,command'
PROCESS_ID = str(os.getpid())

# Functions

def usage(status: int=0) -> None:
    print(f'usage: pgrep.py [-u USER] PATTERN')
    sys.exit(status)

def full_command(process: dict) -> str:
    try:
        return process['COMMAND'] + ' ' + ' '.join(process[None])
    except KeyError:
        return process['COMMAND']

def pgrep(pattern: str, user: Optional[str]=None) -> list[dict]:
    ''' Search process list for matching command pattern and matching user (if
    specified) '''

    processes = []

    with os.popen(PS_COMMAND) as stream:
        for process in csv.DictReader(stream, delimiter=' ', skipinitialspace=True):
            if user and user != process['USER']:
                continue

            if not re.search(pattern, full_command(process)):
                continue

            if PROCESS_ID == process['PID']:
                continue

            processes.append(process)

    return processes

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    user = None
    full = False

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-a': full = True
            case '-u': user = arguments.pop(0)
            case '-h': usage(0)
            case _   : usage(1)

    try:
        pattern = arguments[0]
    except IndexError:
        usage(1)

    for process in pgrep(pattern, user):
        if full:
            print(f'{process["PID"]} {full_command(process)}')
        else:
            print(f'{process["PID"]}')

if __name__ == '__main__':
    main()
