# pylint: skip-file
import sys
sys.path.append("..")
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
import db_func
import article_func


def test_connection_test():
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"


    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def add_to_database_test():
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

def add_article_to_db_test():
    author = "Matti Meikäläinen"
    title = "Tämä on otsikko2"
    journal = "Journal of Journals"
    year = 2020
    volume = 1
    number = 2
    pages = 3
    month = 4
    note = "Tämä on huomautus"
    author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages)
    article = article_func.to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
    db_func.add_article_to_db("testiuser", article)