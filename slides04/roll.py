#!/usr/bin/env python3

''' Simulate rolling dice until you hit snake eyes. '''

import random

# Version 1

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

while (die1 + die2) != 2:
    if die1 == 1 or die2 == 1:
        print(f'! Bruh: {die1}, {die2}')
    else:
        print(f'- Nope: {die1}, {die2}')

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

print(f'+ Yeah: {die1}, {die2}')

# Version 2

while (roll := [random.randint(1, 6), random.randint(1, 6)]) and sum(roll) != 2:
    if 1 in roll:
        print(f'! Bruh: {roll}')
    else:
        print(f'- Nope: {roll}')

print(f'+ Yeah: {roll}')
