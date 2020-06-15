from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('./chromedriver')

def number_active_users(subreddit):
	'''
	Returns number of active users in a subreddit
	Args: Subreddit
	'''

	website = "https://www.reddit.com/r/" + subreddit

	# try:
	# 	page = urlopen(website)
	# except:
	# 	print("error opening url")

	# soup = BeautifulSoup(page, 'html.parser')

	# num_users = soup.find('div', {"class": "currentlyViewingCount"})

	driver.get(website)

	num_users_element = driver.find_elements_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div')[0]

	num_users = num_users_element.text

	print(num_users)

	return num_users

number_active_users("movies")

time.sleep(5)