from pymongo import MongoClient, TEXT

db_name = 'local'
collection_name = 'password'

client = MongoClient('mongodb://host.docker.internal:27017/')
db = client[db_name]
collection = db[collection_name]

if(collection_name not in db.list_collection_names()):
    collection.create_index([('name',1),('username',1)],unique=True)
    collection.insert_one({'name': 'test', 'username': 'hello', 'password': 'world'})

