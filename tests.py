__author__ = 'DaleEMoore@gMail.Com'
# From https://docs.python.org/2/library/unittest.html and others.

#from argparse import ArgumentParser as ArgumentParser2
#import argparse
import copy
import datetime
import os
import shutil
import sys
import time
import unittest2 as unittest

theDir = "testFolder1"
theProgram = "tests.py"

#def setUpModule():
#    print ("setUp before Module")

#def tearDownModule():
#    print ("tearDown after Module")

def createFolder(folderName, timeMod=time.time()):
    print ("Create " + folderName + ". " + theProgram)
    try:
        os.makedirs(folderName)
    except:
        #print ("Folder " + folderName + " already exists.")
        pass
    os.utime(folderName, (timeMod,timeMod))

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("setUp before Class " + theProgram)

        # create folders and files for testing.
        createFolder(theDir)
        createFolder(theDir + os.sep + "d1", time.mktime(time.strptime('16.01.2014 00:00:00', '%d.%m.%Y %H:%M:%S'))) # 16 Jan 2014
        createFolder(theDir + os.sep + "d2", time.mktime(time.strptime('01.05.2015 00:00:00', '%d.%m.%Y %H:%M:%S'))) # 15 May 2015 Friday
        createFolder(theDir + os.sep + "d3", time.mktime(time.strptime('31.12.2014 00:00:00', '%d.%m.%Y %H:%M:%S'))) # 31 December 2014 EOY

        #s1 = theDir + os.pathsep + "d1"
        #time2 = time.mktime(time.strptime('16.01.2014 00:00:00', '%d.%m.%Y %H:%M:%S'))
        # http://stackoverflow.com/questions/21156145/modify-file-create-access-write-timestamp-with-python-under-windows

        # Wait for ENTER to continue doesn't run well in PyCharm test runner.
        #try:
        #    print ("Tap ENTER to continue:")
        #    reply = input("Tap ENTER to continue:")
        #except:
        #    pass


    @classmethod
    def tearDownClass(cls):
        print ("tearDown after Class " + theProgram)

        # delete folders and files from testing.
        print ("Delete all files and folders under " + theDir + ". " + theProgram)
        whatHappened = shutil.rmtree(theDir)
        print ("whatHappened from Delete:" + str(whatHappened) + " " + theProgram)
        """
        TODO; test run this in PyCharm gets  failure here

        whatHappened from Delete:None tests.py

        Process finished with exit code 0

        Error
        Traceback (most recent call last):
          File "/home/dalem/PycharmProjects/RmFilter/tests.py", line 88, in test_rmFilter
            main.main(parser2, argv2)
          File "/home/dalem/PycharmProjects/RmFilter/main.py", line 27, in main
            args = parser2.parse_args()
          File "/usr/lib/python3.4/argparse.py", line 1729, in parse_args
            self.error(msg % ' '.join(argv))
          File "/usr/lib/python3.4/argparse.py", line 2384, in error
            self.exit(2, _('%(prog)s: error: %(message)s\n') % args)
          File "/usr/lib/python3.4/argparse.py", line 2371, in exit
            _sys.exit(status)
        SystemExit: 2

        """

    def test_rmFilter(self):
        print ("\nTest running rmFilter against the folders that have been setup. " + theProgram)

        # TODO; setup args like command line; with something for theDir = "testFolder1"

        # Like: http://stackoverflow.com/questions/24397258/can-not-run-nosetests-when-i-use-argparse-in-my-python-code
        #parser = argparse.ArgumentParser()
        #print ("running:" + parser.prog)
        #parser.add_argument("echo")
        #args = parser.parse_args()
        #print ("args:" + args.echo)

        #parser = ArgumentParser2(description='Remove files and folders from a folder defined by a filter.')
        ##parser = argparse.ArgumentParser(description='Remove files and folders from a folder defined by a filter.')
        #parser.add_argument('--folder', type=str, nargs='+', help='the folder to remove files and folders from.')
        ## --folder is acceptable reduced to -f.
        #parser.add_argument('-rm', action='store_true', default=False, help='remove the files, otherwise just display.')
        #parser.add_argument('--keepfriday', action='store_true', default=False, help='keep files and folders created on Fridays.')

        ## TODO; something like: args = "main.py -folder ."

        ## Like: http://stackoverflow.com/questions/24397258/can-not-run-nosetests-when-i-use-argparse-in-my-python-code
        #parser2 = copy.copy(parser)
        #argv2 = '--foo .'.split()
        ##argv2 = ['--folder','.']
        ##argv2 = copy.copy(sys.argv)
        ##args = parser2.parse_args()
        ## http://stackoverflow.com/questions/18668947/how-do-i-set-sys-argv-so-i-can-unit-test-it

        from argparse import ArgumentParser as ArgumentParser2
        parser2 = ArgumentParser2(description='Remove files and folders from a folder defined by a filter.')
        parser2.add_argument('-folder', type=str, nargs='+', help='the folder to remove files and folders from.')
        parser2.add_argument('-rm', action='store_true', default=False, help='remove the files, otherwise just display.')
        parser2.add_argument('-keepfriday', action='store_true', default=False, help='keep files and folders created on Fridays.')
        # TODO; "args = parser2.parse_args()" causes "unrecognized arguments"
        #    usage: utrunner.py [-h] [-folder FOLDER [FOLDER ...]] [-rm] [-keepfriday]
        #    utrunner.py: error: unrecognized arguments: /home/dalem/PycharmProjects/RmFilter/tests.py::TestStringMethods::test_rmFilter --folder . true
        # It MIGHT be unreasonable to use argparse and unittest2!
        args = parser2.parse_args() # TODO; Causes "unrecognized arguments" because utrunner.py running UnitTests.
        rmDsp = ""
        if args.rm:
            print("Remove filtered files " + theProgram)
            rmDsp = "Remove"
        else:
            print("Display filtered files, do NOT remove. " + theProgram)
            rmDsp = "Do NOT Remove"
        # calculate one week ago for the date comparison
        now = datetime.datetime.now()
        lastWeek = now + datetime.timedelta(days=-7)
        #print('       Now:' + str(now))
        print("Remove files created last week or before:" + str(lastWeek) + ". " + theProgram)

        import rmFilter
        rmFilter.main(parser2, sys.argv, args, lastWeek, rmDsp)

        #import main
        #main.main(parser2, argv2)
        # unit2 runs here because parser is processed twice and uses my default options for rmFilter
        #usage: unit2 [-h] [-folder FOLDER [FOLDER ...]] [-rm] [-keepfriday]
        #unit2: error: unrecognized arguments: --verbose
        #ERROR



    #def setUp(self):
    #    print ("setUp before each test")

    #def tearDown(self):
    #    print ("tearDown after each test")

    #def test_zipper(self):
    #  self.assertEqual('foo'.upper(), 'FOO')

    #def test_upper(self):
    #  self.assertEqual('foo'.upper(), 'FOO')

    #def test_isupper(self):
    #  self.assertTrue('FOO'.isupper())
    #  self.assertFalse('Foo'.isupper())

    #def test_split(self):
    #  s = 'hello world'
    #  self.assertEqual(s.split(), ['hello', 'world'])
    #  # check that s.split fails when the separator is not a string
    #  with self.assertRaises(TypeError):
    #      s.split(2)

    #def test_algebra(self):
    #  self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    print ("Script name=main.")
    # TODO; shouldn't this be args.unittest_args?
    #     sys.argv[1:] = args.unittest_args
    #     unittest2.main()
    theProgram = sys.argv[0]

    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    #itersuite = unittest.TestLoader().loadTestsFromTestCase(MyTestClass)
    runner.run(itersuite)

    #unittest.main()
    print("Done " + theProgram)