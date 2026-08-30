#!/usr/bin/env python3

import requests
import urllib3
import sys

# Constants

URL = 'https://catalog.cse.nd.edu/query.text'

# Functions

def usage(status: int=0):
    print('usage: catalog.py [-t types -o owners]')
    sys.exit(status)

def query_machines(url: str, types: set[str], owners: set[str]) -> list[dict]:
    response = requests.get(URL, verify=False)  # Disable SSL cert check
    machines = []
    machine  = {}

    # Ignore SSL Cert warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for line in response.text.splitlines():
        if not line.strip():                    # Empty line, check filters
            if ((not types  or machine.get('type')  in types) and
                (not owners or machine.get('owner') in owners)):
                machines.append(machine)
            machine = {}                        # Reset current machine
        else:
            key, value = line.split(maxsplit=1)
            machine[key] = value                # Add attributes to current machine

    return machines

# Main Execution

def main(arguments: list[str]=sys.argv[1:]):
    types  = set()
    owners = set()

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-t': types  |= set(arguments.pop(0).split(','))
            case '-o': owners |= set(arguments.pop(0).split(','))
            case '-h': usage(0)
            case _   : usage(1)

    for machine in query_machines(URL, types, owners):
        print(f'{machine["type"]}\t{machine["name"]}\t{machine["owner"]}')

if __name__ == '__main__':
    main()
