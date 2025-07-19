"""
Steps:
    1. Create connection with MongoDB Atlas in Cloud
    2. Select the Database and the Collection, in which you want to work
    3. Create Write Function (insert, delete, update)
            MongoDB : insert_one(), insert_two(), insert_three(), 
                    insert_many () ------> when we need to insert many documents

    4. Create Read Function (retrive/Fetch)
    MongoDB: find()

## STANDARD CLASS -> CAN BE USED FOR PROJECTS DIRECTLY JUST BY UPDATING ----
    
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBHelper:
    
    def __init__(self):
    
    # Create a new client and connect to server
        self.client = MongoClient("mongodb+srv://connectsamiya5904:samiya2025@cluster0.45dsjs4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print('[MongoDBHelper] Connection Created')

    # 2. SELECT THE DATABASE AND THE COLLECTION IN WHICH YOU WANT TO WORk
    def select_db(self, db_name='Agentic_AI', collection='training'):
        self.db = self. client[db_name]
        self.collection= self.db[collection]
        print('[MongoDBHelper] DB {} Collection {} Selected'.format(db_name, collection))

    # 3. Create Insert Function
    def insert(self, document):
        result = self.collection.insert_one(document)
        print('[MongoDBHelper] inserted in collection {}', format(self.collection.name))  
        return result
    
    # 4. Create Delete Function
    def insert(self, document):
        result = self.collection.delete_one(document)
        print('[MongoDBHelper] Document [deleted] in collection {}', format(self.collection.name))  
        return result
    
    # 5. Create Update Function
    def update(self, query, document):
        result = self.collection.update_one(query, {'$set': document})
        print('[MongoDBHelper] Document [Updated] in collection {}'.format(self.collection.name))
        return result
    
    # 6. Create READ Function
    def fetch(self, query=''):
        documents = self.collection.find(query)
        return list(documents)
        print('[MongoDBHelper] Documents [Fetched] from collection {}'.format(self.collection.name))