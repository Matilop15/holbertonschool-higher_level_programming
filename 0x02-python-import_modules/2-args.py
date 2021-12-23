#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argum = argv
    arc = len(argum) - 1
    if arc == 0:
        print("0 arguments.")
    elif arc == 1:
        print("1 argument:\n1: {}".format(argum[1]))
    elif arc > 1:
        print("{:d} argments:".format(arc))
        for a in range(1, arc + 1):
            print("{:d}: {:s}".format(a, argum[a]))
