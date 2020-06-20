#!/usr/bin/ python3

import os
import requests
import re

headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER'))}
subreddit_name = 'movies'

class Subreddit:
	'''
	Subreddit class	that finds the number of active users in a given subreddit over a given timeperiod
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

if __name__ == '__main__':
	sub = Subreddit(subreddit_name, 20, 60)
	sub.number_active_users()