from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["Gen_Ai"]

#collections
chats_collection = db["chat"]
