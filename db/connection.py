# db/connection.py

from pymongo import MongoClient

# Define your MongoDB connection string
# For local MongoDB
LOCAL_CONNECTION_STRING = 'mongodb://localhost:27017/'

# For remote MongoDB (e.g., MongoDB Atlas)
# REMOTE_CONNECTION_STRING = 'mongodb+srv://username:password@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority'

# Create a MongoClient instance
client = MongoClient(LOCAL_CONNECTION_STRING)  # or REMOTE_CONNECTION_STRING for remote

# Access a specific database
db = client['CarRental']


# Optionally, you can provide functions to interact with the database here
def get_Client():
    return db
