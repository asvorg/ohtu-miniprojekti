# pylint: disable=W0611
from pymongo import MongoClient, errors, mongosh


def initialize_database_articles(password_collection):
    """Initialize database connection for the create user function"""
    client = MongoClient('mongodb://localhost:27017/')
    database = client['data']
    password_collection = database[password_collection]
    return password_collection


#def initialize_database_users(user_name):
#    """Initialize database connection for the add password function"""
#    client = MongoClient('mongodb://localhost:27017/')
#    database = client['data']
#    users_collection = database[user_name]
#    return users_collection


def delete_from_passwords(user_name):
    """Initialize database connection for the deletions function"""
    client = MongoClient('mongodb://localhost:27017/')
    database = client['data']
    collection = database[user_name]
    return collection
