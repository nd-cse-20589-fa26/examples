#!/usr/bin/env python3

''' Original
def curl_all(urls: list[str]):
    for url in urls:
        command = ['curl', '-sL', url]
        if (pid := os.fork()) == 0:
            os.execvp(command[0], command)

curl_all(sys.argv[1:])

'''

import os
import sys

import concurrent.futures
import requests
from tqdm import tqdm

def curl_url(url: str):
    response = requests.get(url)
    filename = os.path.basename(url)

    with open(filename, 'wb') as stream:
        stream.write(response.content)

def curl_all(urls: list[str]):
    for url in tqdm(urls):
        curl_url(url)
    '''
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list(tqdm(executor.map(curl_url, urls), total=len(urls)))
    '''

curl_all(sys.argv[1:])
