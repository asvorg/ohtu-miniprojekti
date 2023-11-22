from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi


def test_connection():
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"


    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def add_to_database():
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["bibtex"]
    collection = db["articles"]
    article = {
        "title": "testi",
        "author": "testaaja",
        "year": 2021,
        "journal": "testaus",
        "volume": 1,
        "number": 1,
        "pages": "1-2",
        "month": 1,
        "note": "testi",
        "key": "testi"
    }
    collection.insert_one(article)
    if collection.find_one({"title": "testi"}):
        print("Added to database")

add_to_database()