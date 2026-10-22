#!/usr/bin/env python3

import os
import sys

# Functions

def usage(status: int=0):
    print('''Usage: check flag path
   -e path      Returns if path exists
   -r path      Returns if path is readable
   -x path      Returns if path is executable
   -d path      Returns if path is a directory
   -f path      Returns if path is a regular file
   -s path      Returns if path exists and has size greater than zero
''', file=sys.stderr)
    sys.exit(status)

def is_file_nonempty(path: str) -> bool:
    try:
        return os.stat(path).st_size > 0
    except OSError:
        return False

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    if len(arguments) != 2:
        usage(1)

    flag, path = arguments

    match flag:
        case '-e': sys.exit(0 if os.path.exists(path) else 1)
        case '-r': sys.exit(0 if os.access(path, os.R_OK) else 1)
        case '-x': sys.exit(0 if os.access(path, os.X_OK) else 1)
        case '-d': sys.exit(0 if os.path.isdir(path) else 1)
        case '-f': sys.exit(0 if os.path.isfile(path) else 1)
        case '-s': sys.exit(0 if is_file_nonempty(path) else 1)
        case _   : usage(1)

if __name__ == '__main__':
    main()
