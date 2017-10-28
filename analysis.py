#!/usr/bin/python
import string
import collections

passphrases = []
private_keys = []
public_keys = []
 
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERLETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'

PASSUpperLetterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
PASSLowerLetterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
PASSNumCount = {'1': 0, '2': 0, '3': 0,'4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0,}

PrivateUpperLetterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
PrivateLowerLetterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
PrivateNumCount = {'1': 0, '2': 0, '3': 0,'4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0,}

PublicUpperLetterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
PublicLowerLetterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
PublicNumCount = {'1': 0, '2': 0, '3': 0,'4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0,}

passphrase_dict_count= {}

sum_upper = 0
sum_lower = 0
sum_num =0

def getletterfrequencies(word,type):
	for letter in word:
		if letter in UPPERLETTERS and type =='pass':
			PASSUpperLetterCount[letter] += 1
		if letter in LOWERLETTERS and type =='pass':
			PASSLowerLetterCount[letter] += 1
		if letter in NUMBERS and type =='pass':
			PASSNumCount[letter] += 1
		if letter in UPPERLETTERS and type =='private':
			PrivateUpperLetterCount[letter] += 1
		if letter in LOWERLETTERS and type=='private':
			PrivateLowerLetterCount[letter] += 1
		if letter in NUMBERS and type=='private':
			PrivateNumCount[letter] += 1
		if letter in UPPERLETTERS and type=='public':
			PublicUpperLetterCount[letter] += 1
		if letter in LOWERLETTERS and type=='public':
			PublicLowerLetterCount[letter] += 1
		if letter in NUMBERS and type=='public':
			PublicNumCount[letter] += 1




	return None
'''	

def get_num_lower(thestring):

	return

def get_num_nums(thestring):

	return
'''
with open("temp1mall", "r") as myfile:
	myfile = iter(myfile)
	for line in myfile:
		line = line[:-1]
		passphrases.append(line)
		line = next(myfile)
		line = line[:-1]
		private_keys.append(line)
		line = next(myfile)
		line = line[:-1]
		public_keys.append(line)
		line = next(myfile)

myfile.close


for word in passphrases:
	#passphrase_dict_count =  collections.Counter("upper" if x.isupper() else "lower" if x.islower() else "number" for x in word)
	getletterfrequencies(word,'pass')
	sum_upper += sum(map(str.isupper, word))
	sum_lower += sum(map(str.islower, word))
	sum_num +=  sum(map(str.isdigit, word))

for word in private_keys:
	getletterfrequencies(word, 'private')
for word in public_keys:
	getletterfrequencies(word,'public')

print 'passphrase counts: '
print sorted(PASSUpperLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PASSLowerLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PASSNumCount.items(), key=lambda x: x[1], reverse=True)
print '\n'
print 'private counts: '
print sorted(PrivateUpperLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PrivateLowerLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PrivateNumCount.items(), key=lambda x: x[1], reverse=True)
print '\n'
print 'public counts: '
print sorted(PublicUpperLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PublicLowerLetterCount.items(), key=lambda x: x[1], reverse=True)
print sorted(PublicNumCount.items(), key=lambda x: x[1], reverse=True)

print '\n'

print "passphrase uppers, lowers, nums: "
print sum_upper
print sum_lower
print sum_num
print "percentages: "
print 100*(sum_upper/float(sum_upper + sum_lower + sum_num))
print 100*(sum_lower/float(sum_upper + sum_lower + sum_num))
print 100*(sum_num/float(sum_upper + sum_lower + sum_num))
print "\n"

sum_upper = 0
sum_lower = 0
sum_num =0

for word in private_keys:
	sum_upper += sum(map(str.isupper, word))
	sum_lower += sum(map(str.islower, word))
	sum_num +=  sum(map(str.isdigit, word))

print "private uppers, lowers, nums: "
print sum_upper
print sum_lower
print sum_num
print "percentages: "
print 100*(sum_upper/float(sum_upper + sum_lower + sum_num))
print 100*(sum_lower/float(sum_upper + sum_lower + sum_num))
print 100*(sum_num/float(sum_upper + sum_lower + sum_num))

print "\n"


sum_upper = 0
sum_lower = 0
sum_num =0

for word in public_keys:
	sum_upper += sum(map(str.isupper, word))
	sum_lower += sum(map(str.islower, word))
	sum_num +=  sum(map(str.isdigit, word))

print "public uppers, lowers, nums: "
print sum_upper
print sum_lower
print sum_num
print "percentages: "
print 100*(sum_upper/float(sum_upper + sum_lower + sum_num))
print 100*(sum_lower/float(sum_upper + sum_lower + sum_num))
print 100*(sum_num/float(sum_upper + sum_lower + sum_num))

'''
for privatekey in private_keys:
	private_keys_dict_count = collections.Counter("upper" if x.isupper() else "lower" if x.islower() else "number" for x in privatekey)

for publickey in public_keys:
	public_keys_dict_count = collections.Counter("upper" if x.isupper() else "lower" if x.islower() else "number" for x in publickey)

print passphrase_dict_count
print private_keys_dict_count
print public_keys_dict_count
for label in passphrase_dict_count:
	print label
	if label =="upper":
		sum_upper += passphrase_dict_count[label]
	if label =="lower":
		sum_lower += passphrase_dict_count[label]
	if label == "number":
		sum_num += passphrase_dict_count[label]

print "sum uppers: \n"
print sum_upper
print "\n"
print "sum lowers: \n"
print sum_lower 
print "\n"
print "sum numbers: \n"
print sum_num
print "\n"
'''
