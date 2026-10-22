#!/usr/bin/env python3

import os
import sys

# Functions

def usage(status: int=0):
    print('''Usage: list [directory]
    -R      List the contents of all directories recursively      
''', file=sys.stderr)
    sys.exit(status)

def walk_directory(path: str, recursive: bool=False):
    if not os.path.isdir(path) or not os.access(path, os.R_OK):
        return

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir() and recursive:
                walk_directory(entry.path, recursive)
            elif entry.is_file():
                print(f'{entry.path} {entry.stat().st_size}')

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    recursive = False

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-R': recursive = True
            case '-h': usage(0)
            case _   : usage(1)

    root = arguments[0] if arguments else os.curdir
    walk_directory(root, recursive)

if __name__ == '__main__':
    main()
