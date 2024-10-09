from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

collection = db['test_collection']

collection.create_index("createdAt", expireAfterSeconds=86400)

document = {"name": "test document",
    "createdAt": datetime.utcnow()}

collection.insert_one(document)
client.close()
