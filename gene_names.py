#!/usr/bin/python
from __future__ import print_function
import sys
import re

def help():
    print("Usage: gene_names.py file")
    print("Argument: File to be read")
    print("Use the file Homo_sapiens.GRCh37.75.gtf.gz as an argument and gives the chromosome number, start position and end position for all the genes in the file")

def jsonify(fields, line):
    gene_name = re.search( r'gene_name "(.*?)"', line).group(1)
    chromosome = fields[0]
    start_position = fields[3]
    end_position = fields[4]
    json_string = '{{"geneName":"{}","chr":"{}","startPos":"{}","endPos":"{}"}}'.format(gene_name, chromosome, start_position, end_position)
    print(json_string, end="")

if len(sys.argv) != 2:
    help()
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    once = False
    for line in file:
        fields = line.split('\t')
        if len(fields) < 5 or fields[2] != "gene":
            continue
        start = ",\n\t"
        if once == False:
            once = True
            print("[")
            start = "\t"
        print(start, end="")
        jsonify(fields, line)
    if once == True:
        print("\n]")
