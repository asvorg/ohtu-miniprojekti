import sys
sys.path.append("..")
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
import article_func



def add_article_to_db(user, article):
    '''Add an article to the database'''
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["bibtex"]
    collection = db["articles"]
    article = splice_article(article)
    article = {
        "title": article[0],
        "author": article[1],
        "year": article[2],
        "journal": article[3],
        "volume": article[4],
        "number": article[5],
        "pages": article[6],
        "month": article[7],
        "note": article[8],
        "key": article[9]
    }
    collection.insert_one(article)
    #if collection.find_one({"title": article[0]}):
    #    print(f"Added to database {}")


def splice_article(article):
    '''Splice an article's information into a tuple'''
    #split into list , is delimiter
    article = article.split(",")
    print(article)

article_func.to_bibtex_article()