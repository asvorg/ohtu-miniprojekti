# pylint: disable=W0611
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi


def init_db():
    """Initialize database connection for the create user function"""
    client = MongoClient('mongodb+srv://kaariainenroope:<password>@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/?retryWrites=true&w=majority')
    database = client['data']
    password_collection = database[password_collection]
    return password_collection



#add a article to database
uri = "mongodb+srv://kaariainenroope:<password>@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
