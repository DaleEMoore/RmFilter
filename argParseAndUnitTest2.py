#!/usr/bin/env python

# argParseAndUnitTest2.py

# argparse and unittest don't work well together.
# Figure out how to make argparse and unittest work together and finish rmfilter for Ron Locke at LFI.

# Run like:
# dalem@QnD:~/PycharmProjects/RmFilter$ touch some_file.txt
# dalem@QnD:~/PycharmProjects/RmFilter$ ./argParseAndUnitTest2.py some_file.txt
# dalem@QnD:~/PycharmProjects/RmFilter$ rm some_file.txt

# From http://stackoverflow.com/questions/20265522/argparse-and-unittest-python


__author__ = 'DaleEMoore@gMail.Com'

import argparse
import os
import sys
import datetime
import time

import rmFilter
import unittest

theProgram = "main.py"

class TestThisIsMyClass:
    def main(self):
        #def main(parser2, argv2):

        # calculate one week ago for the date comparison
        now = datetime.datetime.now()
        print("Inside TestThisIsMyClass.main()")
    def test_main(self):
        print("Inside TestThisIsMyClass.test_main()")

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestThisIsMyClass)
    #TODO; fix the following error (this constructor takes no arguments) occurs
    #dalem@QnD:~/PycharmProjects/RmFilter$ ./argParseAndUnitTest2.py some_file.txt
    #Traceback (most recent call last):
    #  File "./argParseAndUnitTest2.py", line 41, in <module>
    #    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestThisIsMyClass)
    #  File "/home/dalem/.pyenv/versions/2.7.5/lib/python2.7/unittest/loader.py", line 56, in loadTestsFromTestCase
    #    loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames))
    #TypeError: this constructor takes no arguments

    runner.run(itersuite)

    print("parser1 coming")
    parser = argparse.ArgumentParser()
    print("parser2 coming")
    parser.add_argument('--input', default='My Input')
    print("parser3 coming")
    parser.add_argument('filename', default='some_file.txt')
    print("parser4 coming")
    parser.add_argument('unittest_args', nargs='*')

    print("parser5 coming")
    args = parser.parse_args()
    print("parser.parse_args() done")
    # TODO: Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()

    theProgram = sys.argv[0]

    TEST = True;
    if TEST:
        print("TEST mode.")
    else:
        print("Not TEST mode.")

    TestThisIsMyClass.main()
