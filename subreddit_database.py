import pymongo
'''
Download MongoDB 4.2.8. Create a new database on localhost called RedditProject.
Create a collection called subreddits
'''
# Creates a connection with MongoClient
client = pymongo.MongoClient('localhost', 27017)
# Create a database called RedditProject
database = client["RedditProject"]
# Create a collection called subreddits
collection = database["subreddits"]
# Test: return a list of your system's databases and collections
# print(client.list_database_names())
# print(database.list_collection_names())

def insert_to_database(subreddit_name, num_users):
    '''
    Creates dict object and inserts to subreddit collection
    '''
    data = {subreddit_name: num_users}
    collection.insert_one(data)

if __name__ == '__main__':
    insert_to_database("showerthoughts", 12)

