#!/usr/bin/python
from warpWallet import generate_keypair
from keyUtils import keyToAddr,privateKeyToWif
import threading, Queue, sys
import string
import random

def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

salt = 'a@b.c'
realtarget = '1MkupVKiCik9iyfnLrJoZLx9RH4rkF3hnA'
temptarget = '1L537cT8Uurxk15xPG1Nv4iPRL9TbBuRXi'
counter =1
for x in range(50000):
	passphrase = id_generator() 
	result = generate_keypair(passphrase, salt)
	private = privateKeyToWif(result)
	public = keyToAddr(result)
	if public[:2] == '1M':
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
		with open("temp1m", "a") as fi:
			fi.write(passphrase +'\n')
			fi.write(private+'\n')
			fi.write(public+'\n')
			fi.write('-------------------------------------------\n')
		fi.close
	with open("temp1mall", "a") as file2:
		file2.write(passphrase +'\n')
		file2.write(private+'\n')
		file2.write(public+'\n')
		file2.write('-------------------------------------------\n')
	file2.close
	print counter
	counter+= 1
'''
#Number of threads
n_thread = 7
#Create queue
queue = Queue.Queue()

class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
    #Assign thread working with queue
        self.queue = queue

    def run(self):
        while True:
        #Get from queue job
            host = self.queue.get()
            print self.getName() + ":" + host
        #signals to queue job is done
            self.queue.task_done()

#Create number process
for i in range(n_thread):
    t = ThreadClass(queue)
    t.setDaemon(True)
    #Start thread
    t.start()

#Read file line by line
f = open("words.txt","r")
for passphrase in f:
	passphrase = passphrase[:-1]
	res = generate_keypair(passphrase, salt)
	private = privateKeyToWif(res)
	public = keyToAddr(res)
	print private
	print public
	print passphrase
	if  public == temptarget:
	            print 'WIN - passphrase:'
	            print passphrase
	            with open("win", "w") as k:
	            	k.write(passphrase)
	            k.close
	            break
	print "result  and counter: "
	print counter
	print res
	counter += 1           
	
f.close()

    #Put line to queue
queue.put(passphrase)
#wait on the queue until everything has been processed
queue.join()


	with open("words.txt") as f:
		for passphrase in f:
			
def mythreads():
	with open("words.txt") as f:
		for passphrase in f:
			passphrase = passphrase[:-1]
			result = generate_keypair(passphrase, salt)
			private = privateKeyToWif(result)
			public = keyToAddr(result)
			print private
			print public
			print passphrase
	            	if  public == temptarget:
	            		print 'WIN - passphrase:'
	            		print passphrase
	            		with open("win", "w") as k:
	            			k.write(passphrase)
	            		k.close
	            		break
	            	print "result  and counter: "
	            	print counter
	            	print result
	            	counter += 1    
	f.close()
	return
'''




