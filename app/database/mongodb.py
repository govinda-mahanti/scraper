from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = "mongodb+srv://gmahanti955_db_user:iIywr8bpPl0nb1LT@cluster0.pmwjcyv.mongodb.net"

if not MONGO_URI:
    raise Exception("MONGO_URI not found. Check GitHub Secrets.")

client = MongoClient(MONGO_URI)

db = client["osint_db"]
collection = db["events"]

print("Connected to MongoDB")

# Prevent duplicate claim_text
collection.create_index("claim_text", unique=True)
collection.create_index("event_datetime_utc")
collection.create_index("country")
collection.create_index("event_type")
collection.create_index("severity_score")
collection.create_index("source_name")

def insert_event(event):
    try:
        collection.insert_one(event)
    except Exception as e:
        print("Insert error:", e)

def get_all_events():
    return list(collection.find({}, {"_id": 0}))