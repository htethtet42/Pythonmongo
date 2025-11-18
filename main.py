import pymongo # for ASCENDING / DESCENDING
from pymongo import MongoClient
from bson import ObjectId # and this line
from datetime import datetime,timezone
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

try:

    mongo_uri = os.getenv("MONGO_URI")

    # Connect to MonoDB Server
    client = MongoClient(mongo_uri)

    # Select database and collection
    db = client["mydatabasemongo"]
    collection = db["employees"]

    # Input document ID (string)
    doc_id =  input("Enter document ID to delete : ").strip()

    try:
        # Convert string to ObjectId
        object_id = ObjectId(doc_id)
    except Exception:   
        print("Invalid ID formant - must be a valid ObjectID string.")
        client.close()
        exit() 

    query_filter = {"_id":object_id}

    # Get document by id
    result = collection.delete_one(query_filter) 

    if result.deleted_count > 0:
        print(f"Delete successfully. Deleted count : {result.deleted_count}")
    else:
        print("No record found with that ID.")        
    
except Exception as e:
    print("Connection Failed : ",e)   
finally:
    #Close connection
    client.close()     




# https://www.mongodb.com/ > Resources > MongoDB Drivers > Python > PyMongo or "Get Started with MongoDB Python" > CRUD Operationss (Asynchronous)