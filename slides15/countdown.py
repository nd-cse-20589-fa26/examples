#!/usr/bin/env python3

class Countdown:

    def __init__(self, n: int=10):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

countdown = Countdown()
print(next(countdown))
print(next(countdown))
print()

for c in countdown:
    print(c)
