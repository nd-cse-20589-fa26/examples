#!/usr/bin/env python3

import subprocess
import sys

# Functions

def usage(status=0):
    print('usage: leetspeak.py [-f chars -t chars]')
    sys.exit(status)

def leetspeak(text: str, mapping: dict[str, str]) -> str:
    ''' Translate each line of text into leetspeak '''
    result = []
    for letter in text:
        result.append(mapping.get(letter.lower(), letter))
    return ''.join(result)

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    fr_chars = 'aeio'
    to_chars = '4310'

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-f': fr_chars = arguments.pop(0)
            case '-t': to_chars = arguments.pop(0)
            case '-h': usage(0)
            case _   : usage(1)

    mapping = {}
    for fr, to in zip(fr_chars, to_chars):
        mapping[fr] = to

    for line in sys.stdin:
        print(leetspeak(line, mapping), end='')

    '''
    # Stream output to cowsay process
    with subprocess.Popen(['cowsay'], stdin=subprocess.PIPE, text=True) as process:
        for line in sys.stdin:
            process.stdin.write(leetspeak(line, mapping))
    '''

if __name__ == '__main__':
    main()
