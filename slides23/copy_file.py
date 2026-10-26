#!/usr/bin/env python3

import os
import sys

from pathlib import Path

# Constants

BUFSIZ = 8 * (1<<10)

# Functions

def copy_file(src: Path, dst: Path):
    try:
        rfd = os.open(src, os.O_RDONLY)
        wfd = os.open(dst, os.O_WRONLY | os.O_CREAT, src.stat().st_mode)
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    while data := os.read(rfd, BUFSIZ):
        os.write(wfd, data)

    os.close(rfd)
    os.close(wfd)

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    if len(arguments) != 2:
        sys.exit(1)

    src, dst = map(Path, arguments)
    copy_file(src, dst)

if __name__ == '__main__':
    main()
