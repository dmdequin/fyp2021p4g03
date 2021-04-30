# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:48:03 2021

@author: ginof
"""

import re
from collections import Counter
import nltk
from nltk.corpus import stopwords


PATH = r'../datasets/irony/test_text.txt'
HATE = r'hate/'

textfile = open(PATH, encoding= 'utf-8')

file_df = []

SPLIT = re.compile(r'[\s\.,;\!\?\"\-\_]')

for line in textfile.readlines():
    words = re.split(SPLIT, line)
    words = [w for w in words if (not w.startswith('@') and \
                                  (not w.startswith('#')) and (w != ""))]
    file_df.append(words)
    

#for row in file_df:
#    for w in row:
        
plain = [w for x in file_df for w in x]
c = Counter(plain)

#print(file_df)
print(c.most_common(10))
#print(stopwords.words('english'))