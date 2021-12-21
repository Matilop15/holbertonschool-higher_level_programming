#!/usr/bin/python3
for i in range(00, 100):
    if (i < 10):
        print('0{:d}'.format(i), end='')

    else:
        print('{:d}'.format(i), end='')

    if (i < 99):
        print(', ', end='')
    if (i == 99):
        print()
