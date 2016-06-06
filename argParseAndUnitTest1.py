#!/usr/bin/env python

# argParseAndUnitTest1.py

# argparse and unittest don't work well together.
# Figure out how to make argparse and unittest work together and finish rmfilter for Ron Locke at LFI.

# Run like:
# dalem@QnD:~/PycharmProjects/RmFilter$ ./argParseAndUnitTest1.py some_file.txt

# From:
# http://stackoverflow.com/questions/1029891/python-unittest-is-there-a-way-to-pass-command-line-options-to-the-app


__author__ = 'DaleEMoore@gMail.Com'

import argparse
import os
import sys
import datetime
import time

import rmFilter
import unittest2

theProgram = "main.py"

def main():
    #def main(parser2, argv2):

    # calculate one week ago for the date comparison
    now = datetime.datetime.now()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='My Input')
    parser.add_argument('filename', default='some_file.txt')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    # TODO: Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest2.main()

    theProgram = sys.argv[0]

    TEST = True;
    if TEST:
        print("TEST mode.")
    else:
        print("Not TEST mode.")

    main()
