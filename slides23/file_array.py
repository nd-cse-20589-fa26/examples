#!/usr/bin/env python3

import os
from dataclasses import dataclass

# Classes

@dataclass
class FileArray:

    path:   str                 # Path to file/array
    size:   int=(1<<10)         # Size of file/array

    def __post_init__(self):
        ''' Post constructor: open file and allocate space. '''
        self.fd = os.open(self.path, os.O_RDWR | os.O_CREAT, 0o644)
        os.posix_fallocate(self.fd, 0, self.size)

    def __del__(self):
        ''' Destructor: close file '''
        os.close(self.fd)

    def __getitem__(self, key: int) -> bytes:
        ''' Get item at key '''
        if key >= self.size:
            raise IndexError

        os.lseek(self.fd, key, os.SEEK_SET)
        return os.read(self.fd, 1)

    def __setitem__(self, key: int, value: bytes):
        ''' Set item at key with value '''
        if key >= self.size:
            raise IndexError

        os.lseek(self.fd, key, os.SEEK_SET)
        os.write(self.fd, value)

array = FileArray('array.txt')
for index, char in enumerate('hello, world'):
    array[index] = char.encode()

for index, char in enumerate('goodbye, all'):
    array[(1<<8) + index] = char.encode()
