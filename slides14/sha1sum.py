#!/usr/bin/env python3

import hashlib
import os
import concurrent.futures
import sys

# Hash Function

def sha1sum(path: str):
    ''' Compute sha1sum digest of the contents of path. '''
    try:
        with open(path, 'rb') as stream:
            return hashlib.sha1(stream.read()).hexdigest()
    except OSError:
        pass

# Compute sha1sum of all arguments

arguments = sys.argv[1:]

'''
# Version 0: Imperative
digests = []
for argument in arguments:
    digests.append(sha1sum(argument))
'''

'''
# Version 1: List comprehension
digests = [sha1sum(argument) for argument in arguments]
'''

'''
# Version 2: Functional Programming
digests = map(sha1sum, arguments)
'''

# Version 3: Functional Programming (with Parallelism)
with concurrent.futures.ProcessPoolExecutor() as executor:
    digests = executor.map(sha1sum, arguments)

# Display sha1sum of all arguments

for argument, digest in zip(arguments, digests):
    print(f'{digest}  {argument}')
