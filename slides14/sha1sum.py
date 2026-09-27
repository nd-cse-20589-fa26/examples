#!/usr/bin/env python3

import hashlib
import os
import concurrent.futures
import sys

# Hash Function

def sha1sum(p):
    with open(p) as stream:
        return hashlib.sha1(stream.read().encode()).hexdigest()

# Create a pool of processes and compute hash in parallel

arguments = sys.argv[1:]

with concurrent.futures.ProcessPoolExecutor(4) as executor:
    hashes = executor.map(sha1sum, arguments)

for p, h in zip(arguments, hashes):
    print(f'{h}  {p}')
