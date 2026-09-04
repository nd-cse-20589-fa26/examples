#!/usr/bin/env python3

import requests
import re
import sys

# Functions

def usage(status: int=0):
    print(f'usage: html_title.py URL')
    sys.exit(status)

def html_images(url: str) -> list[str]:
    ''' Returns all image sources at URL

    >>> html_images('https://pnutz.h4x0r.space/courses/cse.20589.fa26')
    ['static/img/software-systems.png', 'static/img/office-hours.png']
    '''
    response   = requests.get(url)
    img_src_rx = r'<img[^>]+src="([^"]+)"[^>]*>'
    return re.findall(img_src_rx, response.text)

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    if not arguments:
        usage(1)
        
    url = arguments[0]

    for img_src in html_images(url):
        print(img_src)

if __name__ == '__main__':
    main()
