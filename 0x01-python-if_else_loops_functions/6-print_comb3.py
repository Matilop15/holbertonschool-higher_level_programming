#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if ((a != b and a < b) and a < 9):
            if (a == 8 and b == 9):
                print('{0}{1}'.format(a, b))
            else:
                print('{0}{1}, '.format(a, b), end='')
