from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["bibtex"]
collection = db["articles"]

def get_article_from_db_by_user(user):
    for article in collection.find({"user":user}):
        return article

def get_article_from_db_by_cite_key(user, cite_key):
    for article in collection.find({"user": user, "cite_key": cite_key}):
        return article
    
def get_article_from_db_by_author(user, author):
    for article in collection.find({"user": user, "author": author}):
        return article

def get_article_from_db_by_year(user, year):
    for article in collection.find({"user": user, "year": year}):
        return article