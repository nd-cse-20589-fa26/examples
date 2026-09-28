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
    myargs = ['wc', 'ostep-p3.py']
    try:
        os.execvp(myargs[0], myargs)
    except OSError:
        sys.exit(1)
else:       # Parent
    pid, rc_wait = os.wait()
    print(f'hello, I am parent of {rc} (rc_wait:{rc_wait}) (pid:{os.getpid()})')
