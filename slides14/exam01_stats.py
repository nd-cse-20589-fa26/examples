#!/usr/bin/env python3

import csv
import requests

URL = 'https://yld.me/raw/hqQS.csv'
MAX = 40

# Review: Fetching Data

data = requests.get(URL).text.splitlines()

# Compute Individual Scores - Imperative

scores = []
for student in csv.reader(data):        # Discuss: csv.reader
    points = []                         # Dicusss: high-level goal
    for point in student:               # Dicusss: common pattern?
        points.append(float(point))
    scores.append(sum(points))

print(sum(scores))

# Compute Individual Scores - Functional v1

scores = []
for student in csv.reader(data):
    points = sum(map(float, student))   # Discuss: map
    scores.append(points)

print(sum(scores))

# Compute Individual Scores - Functional v2

scores = map(
    lambda student: sum(map(float, student)),
    csv.reader(data)
)

print(sum(scores))

# Compute Individual Scores - List Comprehension v1

scores = [                              # Discuss: list comprehension
    sum(map(float, student))
    for student in csv.reader(data)
]

print(sum(scores))

# Compute Individual Scores - List Comprehension v2

scores = [
    sum([float(point) for point in student])
    for student in csv.reader(data)
]

print(sum(scores))

# Filter scores - Imperative

Bs = []
for score in scores:                    # Discuss: high-level goal
    if .8*MAX <= score < .9*MAX:        # Discuss: common pattern?
        Bs.append(score)

print(len(Bs))

# Filter scores - Functional

Bs = filter(lambda score: .8*MAX <= score < .9*MAX, scores)
print(len(list(Bs)))                    # Discuss: generator

# Filter scores - List Comprehension

Bs = [score for score in scores if .8*MAX <= score < .9*MAX]
print(len(Bs))
