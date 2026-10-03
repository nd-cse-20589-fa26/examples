#!/usr/bin/env python3

import os
import time

# And away we go

print(f'{os.getpid()} Spawning children...')
for i in range(10):
    try:
        pid = os.fork()
    except OSError:
        break

    # Slow it down
    time.sleep(1)
