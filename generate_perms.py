#!/usr/bin/python

from itertools import product
from string import *

keywords = [''.join(i) for i in product(ascii_letters + digits, repeat =  4)]
file = open("perms", "w")

for item in keywords: 
  file.write("%s\n" % item)

file.close()