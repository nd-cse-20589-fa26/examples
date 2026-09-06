#!/usr/bin/env python3

import re

# 0. Read in pokemon data

with open('pokemon.txt') as stream:
    pokemon = stream.read()

# 1. All the strings

print('1. All the strings')
for p in re.findall(r'^.+$', pokemon, flags=re.MULTILINE):
    print(p)
print()

# 2. Only charmander and chespin

print('2. Only charmander and chespin')
for p in re.findall(r'^ch.*$', pokemon, flags=re.MULTILINE):
    print(p)
print()

# 3. All the words with two t's

print('3. All the words with two t\'s')
for p in re.findall(r'^.*t{2}.*$', pokemon, flags=re.MULTILINE):
    print(p)
print()

# 4. Words that don't start with a vowel

print('4. Words that don\'t start with a vowel')
for p in re.findall(r'^[^aeiou].*$', pokemon, flags=re.MULTILINE):
    print(p)
print()

# 5. All words with two consecutive vowels

print('5. All words with two consecutive vowels')
for p in re.findall(r'^.*[aeiou]{2}.*$', pokemon, flags=re.MULTILINE):
    print(p)
print()

# 6. All words with two consecutive letters (same)
print('6. All words with two consecutive letters (same)')
for p in pokemon.splitlines():
    if matched := re.search(r'(.)\1', p):
        print(p)
print()

# 7. All words that begin and end with the same letter
print('7. All words that begin and end with the same letter')
for p in pokemon.splitlines():
    if matched := re.search(r'^(.).*\1$', p):
        print(p)
print()

# 8. All words with exactly 2 of r, s, or t
print('8. All words with exactly 2 of r, s, or t')
for p in pokemon.splitlines():
    if matched := re.search(r'^[^rst]*[rst][^rst]*[rst][^rst]*$', p):
        print(p)
print()
