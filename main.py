__author__ = 'dalem'

# parse command line and get folder(s)
import argparse
import sys

parser = argparse.ArgumentParser(description='Remove files from a folder defined by a filter.')
parser.add_argument('--folder', type=str, nargs='+',
                   help='the folder to remove files from')

args = parser.parse_args()
print ('parser:' + str(parser))
print('args:' + str(args))
print('vars(args):')
vars(args)
print(args.folder)
#TypeError: 'Namespace' object has no attribute '__getitem__'
#print(args['folder'])
#print(parser.parse_args(['--folder']))

#print(args.accumulate(args.integers))

# TODO; iterate through folder(s) and get files older than 1 week.


# TODO; delete selected file
