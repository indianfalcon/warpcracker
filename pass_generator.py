#!/usr/bin/python

import string
import random
def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

file = open("passwords", "w")
for x in range(10):
	y = id_generator() 
  	file.write("%s\n" % y)