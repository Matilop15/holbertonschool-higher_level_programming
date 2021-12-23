#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        a = 'arguments.'
    elif argc == 2:
        a = 'argument:'
    else:
        a = 'arguments:'
    print("{:d} {:s}".format(argc - 1, a))
    for i in range(1, argc - 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
