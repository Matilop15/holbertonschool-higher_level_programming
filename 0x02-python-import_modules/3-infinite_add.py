#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argum = sys.argv
    argc = len(argum)
    suma = 0

    if argc > 1:
        for i in range(1, argc):
            suma += int(argum[i])

    print(suma)
