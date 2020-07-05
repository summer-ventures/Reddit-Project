#!/usr/bin/ python3

import os
import requests
import re
import time
import datetime
import subreddit_database

headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER'))}
subreddit_name = 'science'
length_of_run = 3600
frequency = 60

class Subreddit:
	'''
	Subreddit class	that finds the number of active users in a given subreddit over a given time period
	'''
	def __init__(self, subreddit, runtime, interval):
		self.subreddit = subreddit
		self.runtime = runtime
		self.interval = interval

	def number_active_users(self):
		'''
		Returns number of active users in a subreddit
		Args: Subreddit
		'''

		website = "https://www.reddit.com/r/"

		response = requests.get(website + self.subreddit, headers=headers)

		currently_viewing = re.search(r'(?<=\"currentlyViewingCount\":)\d+', response.text)
		currently_viewing = int(currently_viewing.group(0))

		print(self.subreddit)
		print(currently_viewing)
		
		return currently_viewing

	def run_scraper_over_time(self):
		'''
		Collects data of number of users online in a given subreddit over a given time period 
		at a given interval
		'''
		time_passed = time.clock()

		while time_passed < self.runtime:
			time_read = str(datetime.datetime.now().time().strftime("%H-%M-%S"))
			time_passed = time.clock()
			num_users = self.number_active_users()
			
			subreddit_database.insert_to_database(subreddit_name, time_read, num_users)
			print(time_passed)
			time.sleep(self.interval)
		
	
if __name__ == '__main__':
	sub = Subreddit(subreddit_name, length_of_run, frequency)
	sub.run_scraper_over_time()