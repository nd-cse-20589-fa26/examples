#!/usr/bin/env python3

import csv
import requests

URL = 'https://yld.me/raw/bA7.csv'

# 0. Download data

response = requests.get(URL)            # Review: Requests
lines    = response.text.splitlines()   # Review: splitlines

# 1. With split

for index, line in enumerate(lines):    # Review: enumerate
    if index == 0:
        continue

    # Discuss: destructuring assignment
    netid, last, first, phone = line.split(',')
    print(f'{netid:>8} {phone}')

print()

# 2. With csv.reader

for professor in csv.reader(lines[1:]): # Discuss: csv.reader
    netid, last, first, phone = professor
    print(f'{netid:>8} {phone}')

print()

# 2. With csv.DictReader

for professor in csv.DictReader(lines): # Discuss: csv.DictReader
    print(f'{professor["netid"]:>8} {professor["phone"]}')
