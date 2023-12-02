import sys
sys.path.append("..")
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
from backend.article_func import generate_cite_key, read_user_input_article, to_bibtex_article
from backend.book_func import read_user_input_book, to_bibtex_book


def connect_to_db():
    '''Connect to the database'''
    uri = "mongodb+srv://testiuser:testisalasana123@ohtuminiprojekti-bibtex.19oezdh.mongodb.net/test?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["bibtex"]
    collection = db["articles"]
    return collection, db, client, uri

def add_article_to_db(user, article, tags=None):
    '''Add an article to the database'''
    collection, db, client, uri = connect_to_db()
    article_dict = splice_article(article)
    cite_key = generate_cite_key(article_dict["author"], article_dict["year"])
    #add to database
    article_dict["user"] = user
    article_dict["cite_key"] = cite_key
    if tags:
        article_dict["tags"] = tags
    collection.insert_one(article_dict)

def splice_article(article): #article in bibtex format
    '''Splice the article to a dictionary'''
    article = article.split("\n")
    article = article[1:-1]
    #remove curly brackets
    for i in range(len(article)):
        article[i] = article[i].replace("{", "")
        article[i] = article[i].replace("}", "")
        article[i] = article[i].replace(",", "")
    article_dict = {}
    for i in article:
        i = i.split(" = ")
        article_dict[i[0].strip()] = i[1].strip()
    return article_dict

def splice_book(book): #book in bibtex format
    '''Splice the book to a dictionary'''
    book = book.split("\n")
    book = book[1:-1]
    #remove curly brackets
    for i in range(len(book)):
        book[i] = book[i].replace("{", "")
        book[i] = book[i].replace("}", "")
        book[i] = book[i].replace(",", "")
    book_dict = {}
    for i in book:
        i = i.split(" = ")
        book_dict[i[0].strip()] = i[1].strip()
    return book_dict

def splice_mastersthesis(mastersthesis): #mastersthesis in bibtex format
    '''Splice the master's thesis to a dictionary'''
    mastersthesis = mastersthesis.split("\n")
    mastersthesis = mastersthesis[1:-1]
    #remove curly brackets
    for i in range(len(mastersthesis)):
        mastersthesis[i] = mastersthesis[i].replace("{", "")
        mastersthesis[i] = mastersthesis[i].replace("}", "")
        mastersthesis[i] = mastersthesis[i].replace(",", "")
    mastersthesis_dict = {}
    for i in mastersthesis:
        i = i.split(" = ")
        mastersthesis_dict[i[0].strip()] = i[1].strip()
    return mastersthesis_dict

def get_article_from_db_by_user(user):
    '''Get all articles from the database by user'''
    collection, db, client,uri = connect_to_db()
    articles = list(collection.find({"user":user}))
    return articles

def get_article_from_db_by_cite_key(user, cite_key):
    '''Get an article from the database by cite key'''
    collection, db, client,uri = connect_to_db()
    for article in collection.find({"user": user, "cite_key": cite_key}):
        return article

def get_articles_from_db_by_cite_key(user, cite_key):
    collection, db, client,uri = connect_to_db()
    articles = list(collection.find({"user": user, "cite_key": cite_key}))
    return articles


def get_article_from_db_by_author(user, author):
    '''Get an article from the database by author'''
    collection, db, client,uri = connect_to_db()
    for article in collection.find({"user": user, "author": author}):
        return article

def get_article_from_db_by_year(user, year):
    '''Get an article from the database by year'''
    collection, db, client,uri = connect_to_db()
    for article in collection.find({"user": user, "year": year}):
        return article

def get_articles_from_db_by_tag(user=None, tag=None):
    collection, db, client,uri = connect_to_db()
    articles = list(collection.find({"user": user, "tags": {"$in": [tag]}}))
    return articles

def delete_article_by_cite_key(user,cite_key):
    '''Delete an article from the database'''
    collection, db, client,uri = connect_to_db()
    collection.delete_one({"user": user, "cite_key": cite_key})

def edit_article_by_cite_key(user, cite_key, article): #ei mitää hajua toimiiko tää
    '''Edit an article in the database'''
    old_article = get_article_from_db_by_cite_key(user, cite_key)
    for key in article:
        if article[key]:
            old_article[key] = article[key]

def get_all_articles_from_db():
    '''Get all articles from the database'''
    collection, db, client,uri = connect_to_db()
    articles = list(collection.find({}))
    return articles

def add_book_to_db(user, book, tags=None):
    '''Add a book to the database'''
    collection, db, client, uri = connect_to_db()
    book_dict = splice_book(book)
    cite_key = generate_cite_key(book_dict["author"], book_dict["year"])
    #add to database
    book_dict["user"] = user
    book_dict["cite_key"] = cite_key
    if tags:
        book_dict["tags"] = tags

    collection.insert_one(book_dict)

def add_mastersthesis_to_db(user, mastersthesis, tags=None):
    '''Add a master's thesis to the database'''
    collection, db, client, uri = connect_to_db()
    mastersthesis_dict = splice_mastersthesis(mastersthesis)
    cite_key = generate_cite_key(mastersthesis_dict["author"], mastersthesis_dict["year"])
    #add to database
    mastersthesis_dict["user"] = user
    mastersthesis_dict["cite_key"] = cite_key
    if tags:
        mastersthesis_dict["tags"] = tags

    collection.insert_one(mastersthesis_dict)


#author = "Matti Meikäläinen"
#title = "Tämä on otsikko2"
#journal = "Journal of Journals"
#year = 2020
#volume = 1
#number = 2
#pages = 3
#month = 4
#note = "Tämä on huomautus"
#author, title, journal, year, volume, number, pages, month, note = read_user_input_article(author, title, journal, year, volume, number, pages)
#article = to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
#add_article_to_db("testiuser", article)

author = "Matti Meikäläinen"
editor = "Matti Meikäläinen"
title = "Tämä on otsikko"
publisher = "TÄSSÄ BOOK"
year = 2020
volume = 1
number = 2
series = 3
address = 4
edition = 5
month = 6
note = "Tämä on huomautus"
doi = 7
issn = 8
isbn = 9
author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn = read_user_input_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)

get_article_from_db_by_user("Roope")
