from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBHelper:
    
    def __init__(self):
        # MongoDB Atlas connection
        self.client = MongoClient("mongodb+srv://connectsamiya5904:samiya2025@cluster0.45dsjs4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print('[MongoDBHelper] Connection Created')

    def select_db(self, db_name='Agentic_AI', collection='training'):
        self.db = self.client[db_name]
        self.collection = self.db[collection]
        print('[MongoDBHelper] DB "{}" Collection "{}" Selected'.format(db_name, collection))

    def insert(self, document):
        result = self.collection.insert_one(document)
        print('[MongoDBHelper] Document inserted in collection "{}"'.format(self.collection.name))
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print('[MongoDBHelper] Document deleted from collection "{}"'.format(self.collection.name))
        return result

    def update(self, query, document):
        result = self.collection.update_one(query, {'$set': document})
        print('[MongoDBHelper] Document updated in collection "{}"'.format(self.collection.name))
        return result

    def fetch(self, query={}):
        documents = list(self.collection.find(query))
        print('[MongoDBHelper] Documents fetched from collection "{}"'.format(self.collection.name))
        return documents
