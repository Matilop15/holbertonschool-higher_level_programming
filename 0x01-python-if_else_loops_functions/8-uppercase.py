#!/usr/bin/python3
def uppercase(str):
    c = len(str)
    for b in range(0, c):
        j = ord(str[b])
        if j >= 97 and j <= 123:
            j = j - 32

        print('{:c}'.format(j), end='')
    print()
