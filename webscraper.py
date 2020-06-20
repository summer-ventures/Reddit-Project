#!/usr/bin/ python3

import os
import requests
import re

headers = {'user-agent': 'reddit-{}'.format(os.environ.get('USER'))}

def number_active_users(subreddit):
	'''
	Returns number of active users in a subreddit
	Args: Subreddit
	'''

	website = "https://www.reddit.com/r/"

	response = requests.get(website + subreddit, headers=headers)

	currently_viewing = re.search(r'(?<=\"currentlyViewingCount\":)\d+', response.text)
	currently_viewing = int(currently_viewing.group(0))

	print(subreddit)
	print(currently_viewing)
		
	return currently_viewing

if __name__ == "__main__":
	number_active_users("movies")

'''
joe is here

'''