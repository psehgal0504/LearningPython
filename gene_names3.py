#!/usr/bin/python
from __future__ import print_function
import sys
import re
import json

print("[\n")
with open(sys.argv[1], 'r') as file:
    for line in file:
        if re.search( r'\tgene\t', line, re.M|re.I):
            columns = re.split('\t', line)
            #genes = re.match( r'(.*?)\t.*?\t.*?\t(.*?)\t(.*?)\t.*', line, re.M|re.I)
            genename = re.search( r'gene_name \"(.*?)\";', line, re.M|re. I)
            json_string = '{{"chr":"{}","geneName":"{}","startPos":"{}","endPos":"{}"}}'.format(columns[0], genename.group(1), columns[3], columns[4])
            print("\t",json_string)
    print("\n]")
