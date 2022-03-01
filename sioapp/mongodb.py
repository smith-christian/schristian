from pymongo import MongoClient

# DATABASE_NAME = 'ESI'
# HOST = 'gosmartspaces.com'
# USERNAME = 'schristian'
# PASSWORD = 'smith'
# PORT = '27017'

# cluster =  MongoClient(f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/")
# db = cluster['ESI']
# collection = db['ESI']

#Atlas
DATABASE_NAME = 'ESI'
HOST = 'debug-ipatel.xbcau.mongodb.net'
USERNAME = 'smith'
PASSWORD = 'smith'
# mongodb+srv://smith:smith@debug-ipatel.xbcau.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
cluster =  MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['ESI']
collection = db['ESI']