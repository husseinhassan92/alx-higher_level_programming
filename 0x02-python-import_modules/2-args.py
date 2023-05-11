#!/usr/bin/python3
import sys
n = len(sys.argv)

if n > 1:
    print("{} argument:".format(n-1))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("0 arguments.")
