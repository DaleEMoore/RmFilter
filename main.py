#!/usr/bin/env python
# Command lines
#   Luter at Lucy's Cake Shop is "./rmFilter.py  -folder logs -rm"
#   Ron at LFI wants to keep EOM, EOQ, EOW and dailys for 10 days.
#

__author__ = 'DaleEMoore@gMail.Com'

# parse command line and get folder(s)
from argparse import ArgumentParser as ArgumentParser2
#import argparse
import os
import sys
import datetime
import time

theProgram = "main.py"

def main(parser2, argv2):
    # calculate one week ago for the date comparison
    now = datetime.datetime.now()
    lastWeek = now + datetime.timedelta(days=-7)
    #print('       Now:' + str(now))
    print("Remove files created last week or before:" + str(lastWeek) + ". " + theProgram)
    #date += datetime.timedelta(days=1)


    args = parser2.parse_args()
    rmDsp = ""
    if args.rm:
        print("Remove filtered files " + theProgram)
        rmDsp = "Remove"
    else:
        print("Display filtered files, do NOT remove. " + theProgram)
        rmDsp = "Do NOT Remove"
    #print ('parser:' + str(parser))
    #print('args:' + str(args))
    #print('vars(args):' + str(vars(args)))
    #print(args.folder)
    #TypeError: 'Namespace' object has no attribute '__getitem__'
    #print(args['folder'])
    #print(parser.parse_args(['-folder']))

    #print(args.accumulate(args.integers))

    if args.folder == None:
        print("ERROR: No folders on command line! " + theProgram)
        parser2.print_help()
        return()

    # iterate through folder(s)
    for s1 in args.folder:
        #print('Processing:' + s1)
        for file in os.listdir(s1): # os.walk(s1) walks down the tree.
        #for subdir, dirs, files in os.walk(s1): # os.walk(s1) walks down the tree.
            fullFile = os.path.join(s1, file)
            if not os.path.isdir(fullFile):
                # get files older than 7 days.
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fullFile)
                adate = datetime.datetime.fromtimestamp(atime)
                mdate = datetime.datetime.fromtimestamp(mtime)
                cdate = datetime.datetime.fromtimestamp(ctime)
                if cdate <= lastWeek:
                    print((rmDsp + " " + fullFile + " created: %s" % time.ctime(ctime)) + " " + theProgram)
                    if args.rm:
                        print("Should remove " + fullFile + "  " + theProgram)
                        #os.remove(fullFile)

                    #print((" created: %s" % time.ctime(ctime)))
                    #print(("accessed: %s" % time.ctime(atime)) + " " + str(adate) )
                    #print(("modified: %s" % time.ctime(mtime)) + " " + str(mdate) )
                    #print((" created: %s" % time.ctime(ctime)) + " " + str(cdate) )
                    #print(fullFile)
                    #print(os.path.join(subdir, file)) # us with os.walk()

                    # delete selected file
                    # if -rm on command line kill 'em otherwise just display.
                    # os.remove(fullFile)

        # set mtime for testing. ctime is not create time in Linux.
        # this says it's impossible.
        # http://stackoverflow.com/questions/4537291/setting-creation-or-change-timestamps
        # Perhaps I can create a unit test that would do a good job of faking it out.
    return True

if __name__ == "__main__":
    theProgram = sys.argv[0]
    # TODO; figure out how to tell this program to delete everything except a list of keeps:
    #    Keep Everyday for the last month.
    #    Keep Every Friday for the last quarter.
    #    Keep The first day of every month for the last 2 years.

    parser = ArgumentParser2(description='Remove files and folders from a folder defined by a filter.')
    #parser = argparse.ArgumentParser(description='Remove files and folders from a folder defined by a filter.')
    #print ("running:" + parser.prog)
    parser.add_argument('-folder', type=str, nargs='+', help='the folder to remove files and folders from.')
    parser.add_argument('-rm', action='store_true', default=False, help='remove the files, otherwise just display.')
    parser.add_argument('-keepfriday', action='store_true', default=False, help='keep files and folders created on Fridays.')
    #parser.add_argument('-b', action='store_true', default=False)
    #parser.add_argument('-rm', type=str, nargs='+', help='remove the files, otherwise just display')

    main(parser, sys.argv)
