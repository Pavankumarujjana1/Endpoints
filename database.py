from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://admin:user143@cluster0.mdprjc3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGODB_URL)
db = client["user_db"]
user_collection = db["username"]  

