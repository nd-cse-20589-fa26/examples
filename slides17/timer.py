#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional

import sys
import time

''' Version 1

class Timer:
    def __init__(self, start_time: Optional[float]=None):
        self.start_time = start_time or time.time()
        self.stop_time  = 0.0

    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time

    def __str__(self) -> str:
        return f'Timer({self.start_time}, {self.stop_time})'

timer = Timer()
print(timer)

print(timer.elapsed_time())
time.sleep(1)
print(timer.elapsed_time())
time.sleep(1)

timer.stop()
time.sleep(1)
print(timer.elapsed_time())
'''

''' Version 2 '''

@dataclass
class Timer:
    start_time: float = time.time()
    stop_time:  float = 0.0

    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    @property
    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

with Timer() as timer:
    for _ in range(5):
        print(f'Loop: {timer.elapsed_time:0.2f}')
        time.sleep(1)

time.sleep(5)

print(f'Final: {timer.elapsed_time:0.2f}')
