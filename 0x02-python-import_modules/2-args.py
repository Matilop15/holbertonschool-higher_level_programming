#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arc = len(sys.argv)
    if arc == 1:
        print("0 arguments.")
    elif arc == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(arc - 1, sys.argv[1]))
    else:
        print("{:d} argments:".format(arc - 1))
        for a in range(1, arc):
            print("{:d}: {:s}".format(a, sys.argv[a]))
