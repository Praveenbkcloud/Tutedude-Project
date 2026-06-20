from pymongo import MongoClient

MONGO_URI = "your_connection_string"

client = MongoClient(MONGO_URI)

print("Connected Successfully")