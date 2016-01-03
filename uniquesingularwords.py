__author__ = 'John Moon'
###################
#
# Github Repo: https://github.com/johncdwall/uniquesingularwords
# Contact: github@cdwall.com

import sys
from textblob import TextBlob

# file name should be first command line argument
sourcefilename = sys.argv[1]
if (sourcefilename == ''):
    print "Usage: python uniquesingularwords.py [source file name]"
    exit()

try:
    #read entire file into string
    with open (sourcefilename, 'r') as srcfile:
        textfromfile = srcfile.read()
except:
    print "unable to read file %s" % sourcefilename

# make textblob object from text string read from file
text = TextBlob(textfromfile)

# dictionary to hold counts of unique sigular words
uniquewords = {}

# loop through each word, convert to singular and count
for i in range(0,len(text.words)):
    singularword = text.words[i].singularize()
    try:
        uniquewords[singularword] += 1
    except:
        uniquewords[singularword] = 1

# print counts
for key in sorted(uniquewords.keys()):
    print key,uniquewords[key]