#!/usr/bin/python
from __future__ import print_function
import sys
import re
import json

gene_data = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        if re.search( r'\tgene\t', line, re.M|re.I):
            genes = re.match( r'(.*?)\t.*?\t.*?\t(.*?)\t(.*?)\t.*', line, re.M|re.I)
            gene_info = {}
            genename = re.search( r'gene_name \"(.*?)\";', line, re.M|re. I)
            gene_info["geneName"] = genename.group(1)
            gene_info["chr"] = genes.group(1)
            gene_info["startPos"] = genes.group(2)
            gene_info["endPos"] = genes.group(3)
            gene_data.append(gene_info)
    print(json.dumps(gene_data, indent=4, separators=(',', ': ')))
