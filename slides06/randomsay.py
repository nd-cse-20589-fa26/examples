#!/usr/bin/env python3

import os
import subprocess
import random                           # Discuss: random module
import sys

# Constants
                                        # Discuss: set data structure
FORBIDDEN = {'bong', 'sodomized', 'kiss', 'head-in', 'satanic', 'telebears'}

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    cows = []                           # Discuss: os.popen
    for index, line in enumerate(os.popen('cowsay -l')):
        if not index:                   # Discuss: enumerate
            continue

        for cow in line.split():        # Review: str.split
            if cow not in FORBIDDEN:    # Review: searching collection
                cows.append(cow)        # Review: list.append
    
    command = ['cowsay', '-f', random.choice(cows)] + arguments
    subprocess.run(command, check=True) # Variant: os.system

if __name__ == '__main__':
    main()
