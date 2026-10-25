#!/usr/bin/env python3

import os
import stat
import sys

from dataclasses import dataclass
from itertools import cycle
from pathlib import Path

# Classes

class PathEntry(Path):
    @property
    def path(self):
        return self.parent / self

class WalkerFactory:
    @classmethod
    def get_walker(cls, entry: os.DirEntry | PathEntry, recursive: bool=False):
        match stat.S_IFMT(entry.stat().st_mode):
            case stat.S_IFREG: return FileWalker(entry)
            case stat.S_IFDIR: return DirectoryWalker(entry) if recursive else BaseWalker(entry)
            case _:            return BaseWalker(entry)

@dataclass
class BaseWalker:
    entry:  os.DirEntry | PathEntry

    def walk(self, recursive: bool=False):
        pass

class FileWalker(BaseWalker):
    def walk(self, recursive: bool=False):
        print(f'{self.entry.path} {self.entry.stat().st_size}')

class DirectoryWalker(BaseWalker):
    def walk(self, recursive: bool=False):
        try:
            with os.scandir(self.entry.path) as entries:
                for entry in map(WalkerFactory.get_walker, entries, cycle([recursive])):
                    entry.walk(recursive)
        except PermissionError:
            pass

# Functions

def usage(status: int=0):
    print('''Usage: list [directory]
    -R      List the contents of all directories recursively
''', file=sys.stderr)
    sys.exit(status)

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    recursive = False

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-R': recursive = True
            case '-h': usage(0)
            case _   : usage(1)

    root = arguments[0] if arguments else os.curdir
    DirectoryWalker(PathEntry(root)).walk(recursive)

if __name__ == '__main__':
    main()
