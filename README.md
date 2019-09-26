# LearningPython
> This repository contains 3 python programs:
- [Circumference.py](circumference.py)
- [areaCode.py](areaCode.py)
- [gene_names.py](gene_names.py), [gene_names2.py](gene_names2.py) and [gene_names3.py](gene_names3.py) (is the same program but involves different syntaxes for achieving the same function)
## Circumference.py
> This creates a basic python script called circumference.py that assigns pi to 3.14159 and prints the circumference of a circle given a second variable radius with the initial value of 3.  
> The radius is defines within the script.  
> The output prints:
```
The circumference of a circle of radius 3 is 18.84954
```
## areaCode.py
> Create a basic python script called areaCode.py that begins as:
```
#!/usr/bin/python
from __future__ import print_function
import re
phone = "602-343-8747"
```
> and prints out the area code as
```
The area code is: 602
```
> where the area code is extracted using regular expressions.
## gene_names.py, gene_names2.py and gene_names3.py
> For this script, you’ll need to have access to a dataset and I would like you to put the dataset in a different directory.  
- > First, download the file, Homo_sapiens.GRCh37.75.gtf.gz, from http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens using `wget, and place this file within a directory called data within your home directory. 
- > Unzip this file with gunzip, gunzip Homo_sapiens.GRCh37.75.gtf.gz  
- > The command head ~/data/Homo_sapiens.GRCh37.75.gtf should give the start of the file 
```
#!genome-build GRCh37.p13
```
- > Second, create a python script called gene_names.py that takes a gtf file (which you downloaded one of them) as an argument, and spits out the gene_name, the chromosome (the first column), the starting position (the fourth column), and the ending position (the fifth column) for only those columns where the third column is “gene”.  
- > Columns within the file are tab-delimited. The result should be JSON format:
```
./gene_names ~/data/Homo_sapiens.GRCh37.75.gtf
[
  {"geneName":"OR4G4P","chr":"1","startPos":52473, "endPos":54936},
  ... 
]
```
- > where ... are additional genes
