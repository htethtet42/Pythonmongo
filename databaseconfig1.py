from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB server
client = MongoClient(mongo_uri)

# Select database
db = client["mydatabase"]

# Get Firebase client
# db = firestore.client()

def dbconnect():
    return db



