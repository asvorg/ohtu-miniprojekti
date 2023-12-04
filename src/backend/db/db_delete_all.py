from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

def connect_to_db():
    '''Connect to the database'''
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["bibtex"]
    collection = db["articles"]
    return collection, db, client, uri

def delete_all_from_db():
    '''CARE'''
    collection, db, client,uri = connect_to_db()
    result = collection.delete_many({})

    # Print the result
    print(f"{result.deleted_count} document(s) deleted")

    # Close the MongoDB connection
    client.close()


delete_all_from_db()