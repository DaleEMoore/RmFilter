#!/usr/bin/env python

import os
#import sys
import datetime
import time

theProgram = "rmFilter.py"

def main(parser2, argv2, args, lastWeek, rmDsp):
    ## iterate through folder(s)
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
                    pass
                pass
            pass
        pass
    return True

if __name__ == "__main__":
	print ("I expect you to import this in someOther.py program.")
	#theProgram = sys.argv[0]
	## TODO; figure out how to tell this program to delete everything except a list of keeps:
	##    Keep Everyday for the last month.
	##    Keep Every Friday for the last quarter.
	##    Keep The first day of every month for the last 2 years.
	#parser = ArgumentParser2(description='Remove files and folders from a folder defined by a filter.')
	#parser.add_argument('-folder', type=str, nargs='+', help='the folder to remove files and folders from.')
	#parser.add_argument('-rm', action='store_true', default=False, help='remove the files, otherwise just display.')
	#parser.add_argument('-keepfriday', action='store_true', default=False, help='keep files and folders created on Fridays.')
	#main(parser, sys.argv)
