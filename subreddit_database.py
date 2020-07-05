import pymongo
from webscraper import subreddit_name
'''
Create a new database on called RedditProject.
Create a collection called subreddits_user_count
'''
database_name = "RedditProject"
collection_name = subreddit_name
# Creates a connection with MongoClient
cluster = pymongo.MongoClient("mongodb+srv://Alex:12345@redditproject.ft4yu.mongodb.net/test")
# Create a database called RedditProject
database = cluster[database_name]
# Create a collection called subreddits
collection = database[collection_name]

def insert_to_database(subreddit_name, time_read, num_users):
    '''
    Creates dict object and inserts to subreddit collection
    '''
    data = {"subreddit name": subreddit_name,  "time": time_read, "number of users": num_users}
    collection.insert_one(data)

if __name__ == '__main__':
    insert_to_database("showerthoughts", "1-1-1", 12)

