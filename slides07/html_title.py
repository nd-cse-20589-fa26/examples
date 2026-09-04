#!/usr/bin/env python3

import requests
import re
import sys

from typing import Optional

# Constants

HTML_TITLE_RX = r'<head>.*<title>([^<]+)</title>.*</head>'

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

    if title := re.search(HTML_TITLE_RX, response.text, flags=re.DOTALL):
        return title[1]

    return None

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    try:
        url = arguments[0]
    except IndexError:
        usage(1)

    print(html_title(url))

if __name__ == '__main__':
    main()
