#!/usr/bin/python
import os
import sys
import datetime
import time
from twython import Twython
from random import randint

def test():

	#if I can get this to work, random hour and random minute
	hour = randint(0,23)
	minute = randint(0,59)

	#open cat facts!
	#filename = 'cat_facts.txt'
	#open file and read file into list(array) without the newlines
	with open('cat_facts.txt') as f:
		lines = f.read().splitlines()
	#close the file
	f.close()
	#debug file opening in append mode
	test = open('test.txt', 'a')
	#debug = open('debug.txt','a')
	
	while(1):
		#until I can workout a random time, pick a time between 1 minute and 24 hours
		wait = randint(60,86400)
		test_out = 'Waiting: ' + str(wait) + ' seconds '
		test.write(test_out)
		#counter for use in the while loop
		counter = False
		#the target is the twitter handle we want to bother
		target = '<person to bother>'
		#choose a tweet, if it is too long pick another
		while(counter == False):
			fact = randint(0, len(lines)-1)
			tweet = str(target + lines[fact])
			if(len(tweet)<=140):
				counter = True
				test_out = 'Chose fact number: ' + str(fact) + '\n'
				test.write(test_out)
		#debug.write(tweet)
		#connect to Twitter
		#application key
		APP_KEY = '<redacted>'
		#application secret
		APP_SECRET = '<redacted>'
		#User OAUTH tokens
		OAUTH_TOKEN = '<redacted>'
		#user OAUTH secret
		OAUTH_SECRET = '<redacted>'
	
		twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_SECRET)
		twitter.verify_credentials()
	
		twitter.update_status(status=tweet)
		time.sleep(wait)


test()
