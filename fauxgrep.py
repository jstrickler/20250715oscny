import sys
import fileinput
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux Grep")
parser.add_argument('-f', dest="show_file_names", action="store_true", help="Show file names")
parser.add_argument("search_term", help="term to find")
parser.add_argument("files", nargs="*", help="files to search")

args = parser.parse_args()

for raw_line in fileinput.input(args.files):
    if args.search_term in raw_line:
        line = raw_line.rstrip()
        if args.show_file_names:
            print(fileinput.filename(), end=" ")
        print(line)