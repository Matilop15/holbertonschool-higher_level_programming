#!/usr/bin/python3
def print_last_digit(number):
    
    if number < 0:
        number = -number

    numb = number % 10

    print('{:d}'.format(numb), end='')
    return numb
