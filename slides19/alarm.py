#!/usr/bin/env python3

import os
import signal
import sys
import time

def handle_sigalrm(signum, frame):
    print(f'Alarm triggered... Killing {pid}!')
    os.kill(pid, signal.SIGKILL)

    _, status = os.wait()
    print(f'Child {pid} exited with {os.WTERMSIG(status)}')
    sys.exit(0)


match pid := os.fork():
    case 0: # Child
        while True:
            print('Hahahaha')
            time.sleep(1)

    case _: # Parent
        signal.signal(signal.SIGALRM, handle_sigalrm)
        signal.alarm(5)

        while True:
            print('Waiting...')
            time.sleep(1)
