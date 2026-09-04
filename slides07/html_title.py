#!/usr/bin/env python3

import requests
import re
import sys

from typing import Optional

# Functions

def usage(status: int=0):
    print(f'usage: html_title.py URL')
    sys.exit(status)

def html_title(url: str) -> Optional[str]:
    ''' Returns HTML title at URL

    >>> html_title('https://nd.edu')
    'University of Notre Dame'
    '''
    response = requests.get(url)
    title_rx = r'<head>.*<title>([^<]+)</title>.*</head>'

    if title := re.search(title_rx, response.text, flags=re.DOTALL):
        return title[1]

    return None

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    if not arguments:
        usage(1)

    url = arguments[0]
    print(html_title(url))

if __name__ == '__main__':
    main()
