#!/usr/bin/python

import sys


def main():
    print 'Hello there,', sys.argv[1]

# only execute if python interprets this as main
if '__main__' == __name__:
    main()


