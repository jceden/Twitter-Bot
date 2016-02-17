#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
from twython import Twython
from random import randint

def makelist ( filename ):
	#open file and read file into list(array) without the newlines
	with open(filename) as f:
		mylist = f.read().splitlines()
	#close the file
	f.close
	return mylist

def test():

	#open cat facts!
	filename = 'cat_facts.txt'

	while(1):
		#until I can workout a random time, pick a time between 1 minute and 24 hours
		wait = randint(60,86400)
		test_out = 'Waiting: ' + str(wait) + ' seconds '
		test.write(test_out)
		lines = []
		lines = makelist( filename )
		#counter for use in the while loop
		counter = False
		#the target is the twitter handle we want to bother
		target = '<enter a twitter handle'
		#choose a tweet, if it is too long pick another
		while(counter == False):
			fact = randint(0, len(lines)-1)
			tweet = str(target + lines[fact])
			if(len(tweet)<=140):
				counter = True
		#connect to Twitter
		#application key
		APP_KEY = ''
		#application secret
		APP_SECRET = ''
		#User OAUTH tokens
		OAUTH_TOKEN = ''
		#user OAUTH secret
		OAUTH_SECRET = ''
	
		twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_SECRET)
		twitter.verify_credentials()
	
		twitter.update_status(status=tweet)
		time.sleep(wait)


test()
