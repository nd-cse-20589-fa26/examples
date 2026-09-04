#!/usr/bin/env python3

import requests
import re
import sys

from typing import Optional

# Functions

def usage(status: int=0):
    print(f'usage: html_title.py URL')
    sys.exit(status)

def html_body(url: str) -> Optional[str]:
    ''' Returns body title at URL

    >>> html_body('https://example.com')
    '<div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div>'
    '''
    response = requests.get(url)
    body_rx  = r'<body>(.*)</body>'

    if body := re.search(body_rx, response.text, flags=re.DOTALL):
        return body[1]

    return None

def strip_html(text: str) -> str:
    ''' Remove HTML tags from text

    >>> strip_html('<p><b>a b c</b></p>')
    'a b c'
    '''
    tag_rx = r'<[^>]+>'
    return re.sub(tag_rx, ' ', text).strip()

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    if not arguments:
        usage(1)

    url = arguments[0]
    if body := html_body(url):
        print(strip_html(body))

if __name__ == '__main__':
    main()
