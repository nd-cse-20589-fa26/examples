#!/usr/bin/env python3

from typing import Iterable, Iterator

# Constants

CHUNKS = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Iterator

class Flatten:

    def __init__(self, sequence: Iterable[Iterable[int]]):
        self.sequence = sequence

    def __iter__(self):
        # Create iterator for all subsequences, and get first one
        self.all_iterators    = map(iter, self.sequence)
        self.current_iterator = next(self.all_iterators)
        return self

    def __next__(self):
        # Attempt to get element from current iterator
        # - Go to next iterator if current one is exhausted
        # - If all iterators are exhausted, then StopIteration will be raised

        element = None

        while element is None:
            try:
                element = next(self.current_iterator)
            except StopIteration:
                self.current_iterator = next(self.all_iterators)

        return element

# Generator

def flatten(sequence: Iterable[Iterable[int]]) -> Iterator[int]:
    ''' Version 0
    for subsequence in sequence:
        for element in subsequence:
            yield element
    '''

    ''' Version 1 '''
    for subsequence in sequence:
        yield from subsequence

# Main Execution

for number in CHUNKS:
    print(number)

print()

for number in Flatten(CHUNKS):
    print(number)

print()

for number in flatten(CHUNKS):
    print(number)

print()
