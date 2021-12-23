#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(argc - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc - 1))
        for a in range(1, argc):
            print("{:d}: {:s}".format(a, sys.argv[a]))
