#!/usr/bin/env python3

import sys

# Functions

def fizzbuzz(start: int=1, stop: int=100) -> None:
    '''
    >>> fizzbuzz(1, 5)
    1
    2
    Fizz
    4
    Buzz

    >>> fizzbuzz(12, 15)
    Fizz
    13
    14
    FizzBuzz
    '''
    for number in range(start, stop + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

# Main Execution

def main(arguments: list=sys.argv[1:]) -> None:
    '''
    >>> main(['1', '5'])
    1
    2
    Fizz
    4
    Buzz

    >>> main(['12', '15'])
    Fizz
    13
    14
    FizzBuzz
    '''
    try:
        start = int(arguments[0])
    except IndexError:
        start = 1

    try:
        stop  = int(arguments[1])
    except IndexError:
        stop  = 100

    fizzbuzz(start, stop)

if __name__ == '__main__':
    main()
