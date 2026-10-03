#!/usr/bin/env python3

import os
import signal
import sys
import time

# And away we go

print(f'Spawning children...')
for i in range(10):
    match pid := os.fork():
        case 0: # Child
            print(f'Child process: {os.getpid()}')
            time.sleep(i)
            sys.exit(i)

# Fix 1: Wait all

print(f'Waiting for children...')
for i in range(10):
    pid, status = os.wait()
    print(f'Child {pid} exited with {os.WEXITSTATUS(status)}')

# Fix 2: Wait after signal
    
WaitedChildren = []

def handle_sigchld(signum, frame):
    pid, status = os.wait()
    print(f'Child {pid} exited with {os.WEXITSTATUS(status)}')
    WaitedChildren.append(pid)
   
print()
print(f'Registering handler...')
signal.signal(signal.SIGCHLD, handle_sigchld)

print(f'Spawning children...')
for i in range(10):
    match pid := os.fork():
        case 0: # Child
            print(f'Child process: {os.getpid()}')
            time.sleep(i)
            sys.exit(i)

while len(WaitedChildren) < 10:
    print('Waiting...')
    time.sleep(1)
