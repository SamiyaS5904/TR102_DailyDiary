"""
    MONGO DB

    We are using MongoDB in Cloud (MongoDB Atlas)
    -> Databse in the Cloud, which stores data as documents.
        STEPS :-
        1. Signup/Register 
        2. Create a cluster (AWS | GCP | AZURE )
            select region which is nearest (eg. Delhi, if not available Mumbai )
            eg. GCP, in gcp there is a virtual machine --          
        3. Network Acess -> 0.0.0/0 (you can access from anywhere)
        4. Database Acess -> to create a user --


    ->  In MongoDb we dont have tables, we have collections
    -> A Collection is like a folder

    -> We dont have rows, we have documnets
    A Document is typically a JSON Document which get stored inside the collection

    Hence MongoDB is a NoSQL DataBase
            
            
    (SQL -- Relational Database, we did both SQL, NoSQL (MongoDB))
            
"""



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://connectsamiya5904:samiya2025@cluster0.45dsjs4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


"""
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""

db = client['Agentic_AI']
collections = db.list_collection_names()
print(collections)