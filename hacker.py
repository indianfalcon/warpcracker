#!/usr/bin/python
from warpWallet import generate_keypair
from keyUtils import keyToAddr,privateKeyToWif
import threading, Queue, sys
import string
import random
import urllib2
from lxml import html
import requests


def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

salt = 'a@b.c'
realtarget = '1MkupVKiCik9iyfnLrJoZLx9RH4rkF3hnA'
temptarget = '1L537cT8Uurxk15xPG1Nv4iPRL9TbBuRXi'
counter =1

f = open("wordlist10k.txt","r")
for passphrase in f:
	passphrase = passphrase[:-1]
	res = generate_keypair(passphrase)
	private = privateKeyToWif(res)
	publicaddress = keyToAddr(res)
	requesturl = 'https://blockchain.info/address/' + publicaddress
	page = requests.get(requesturl)
	sourceCode = page.content
	htmlElem = html.document_fromstring(sourceCode)
	tdElems = htmlElem.cssselect("[id=final_balance]")
	for elem in tdElems:
		text = elem.text_content()

	text = text.partition(' ')[0]
	balance = float(text)
	if balance > 0:
		print "yay got some balance!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print balance
		print publicaddress
		print private
		print passphrase
		with open("win2", "a") as k:
			k.write(passphrase)
	else:
		print "balance is zero"
		print publicaddress
		print counter

	counter +=1
#pubaddress = '1MkupVKiCik9iyfnLrJoZLx9RH4rkF3hnA'




'''


for x in range(5000):
	passphrase = id_generator() 
	result = generate_keypair(passphrase, salt)
	private = privateKeyToWif(result)
	public = keyToAddr(result)
	print private
	print public
	print passphrase
	if  public == realtarget:
		print 'WIN - passphrase:'
		print passphrase
		with open("win", "w") as k:
		            k.write(passphrase)
		k.close
		break
	print "result  and counter: "
	print counter
	counter+= 1
	'''