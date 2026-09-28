#!/usr/bin/env python3

import os
import sys

print(f'hello world (pid:{os.getpid()})')

try:
    rc = os.fork()
except OSError:
    print('fork failed', file=sys.stderr)
    sys.exit(1)

if rc == 0: # Child (new process)
    print(f'hello, I am child (pid:{os.getpid()})')
else:       # Parent
    print(f'hello, I am parent of {rc} (pid:{os.getpid()})')
