#!/usr/bin/env python

__author__ = 'dalem'

# parse command line and get folder(s)
import argparse
import os
import sys
import datetime
import time

# TODO; calculate one week ago for the date comparison
now = datetime.datetime.now()
lastWeek = now + datetime.timedelta(days=-7)
#print('       Now:' + str(now))
print("Remove files created last week or before:" + str(lastWeek))
#date += datetime.timedelta(days=1)


parser = argparse.ArgumentParser(description='Remove files from a folder defined by a filter.')
parser.add_argument('-folder', type=str, nargs='+', help='the folder to remove files from')
parser.add_argument('-rm', action='store_true', default=False, help='remove the files, otherwise just display')
#parser.add_argument('-b', action='store_true', default=False)
#parser.add_argument('-rm', type=str, nargs='+', help='remove the files, otherwise just display')

args = parser.parse_args()
rmDsp = ""
if args.rm:
    print('Remove filtered files')
    rmDsp = "Remove"
else:
    print('Display filtered files, do NOT remove')
    rmDsp = "Do NOT Remove"
#print ('parser:' + str(parser))
#print('args:' + str(args))
#print('vars(args):' + str(vars(args)))
#print(args.folder)
#TypeError: 'Namespace' object has no attribute '__getitem__'
#print(args['folder'])
#print(parser.parse_args(['--folder']))

#print(args.accumulate(args.integers))

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
                print((rmDsp + " " + fullFile + " created: %s" % time.ctime(ctime)))
                if args.rm:
                    print("Should remove " + fullFile)
                    #os.remove(fullFile)

                #print((" created: %s" % time.ctime(ctime)))
                #print(("accessed: %s" % time.ctime(atime)) + " " + str(adate) )
                #print(("modified: %s" % time.ctime(mtime)) + " " + str(mdate) )
                #print((" created: %s" % time.ctime(ctime)) + " " + str(cdate) )
                #print(fullFile)
                #print(os.path.join(subdir, file)) # us with os.walk()

                # TODO; delete selected file
                # TODO; if --kill on command line kill 'em otherwise just display.
                # os.remove(fullFile)

    # TODO; set ctime for testing?
    # this says it's impossible.
    # http://stackoverflow.com/questions/4537291/setting-creation-or-change-timestamps
    # Perhaps I can create a unit test that would do a good job of faking it out.
