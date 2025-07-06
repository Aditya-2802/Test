from pymongo import MongoClient

client = MongoClient("mongodb+srv://Aditya28:JqiJYcVXcrugeGO3@cluster0.dzs3uyq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)  # or use MongoDB Atlas URL
db = client['Aditya']
collection = db['git']

def insert_event(data):
    collection.insert_one(data)

def get_all_events():
    return list(collection.find().sort("timestamp", -1))
