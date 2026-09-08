#!/usr/bin/env python3

# Constants

URL = 'https://pnutz.h4x0r.space/courses/cse.20589.fa26'

# 0. Fetch data using curl

import os

with os.popen(f'curl -sL {URL}') as stream:
    text = stream.read()

# 1. Fetch data using requests

import requests

response = requests.get(URL)
text     = response.text

# 2. Extract title using regex

import re

if matched := re.search(r'<title>([^<]+)</title>', text):
    print(f'Title is: {matched[1]}')

# 3. Extract images using regex

for img_source in re.findall(r'<img src="([^"]+)"[^>]*>', text):
    print(img_source)
