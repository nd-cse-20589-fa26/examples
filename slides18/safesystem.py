#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional

import os
import time

# Class

@dataclass
class SafeSystem:
    command:    list[str]

    pid:        Optional[int] = None
    status:     Optional[int] = None

    @property
    def state(self):
        if self.status is None:
            return 'Running'

        return f'Terminated ({os.WEXITSTATUS(self.status)})'

    # Context Manager Protocol

    def __enter__(self):
        self.pid = os.fork()

        if self.pid == 0:   # Child
            try:
                os.execvp(self.command[0], self.command)
            except OSError:
                os._exit(1)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _, self.status = os.waitpid(self.pid, 0)

# Main Execution

with SafeSystem(['ls', '-l']) as process:
    for i in range(10):
        time.sleep(0.1)
        print(f'{i}: {process.state}')

print(f'Final: {process.state}')
