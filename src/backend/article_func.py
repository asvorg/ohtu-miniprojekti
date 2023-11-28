'''Functions for handling article information'''
import datetime


def read_user_input_article(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
    '''Read user input and return a tuple of the paper's information'''
    if not author or not title or not journal or not year:
        raise ValueError("Author, title, journal and year are required fields")
    year = int(year)
    volume = int(volume)
    number = int(number)
    pages = int(pages)
    if year < 0 or year > datetime.datetime.now().year:
        raise ValueError("Invalid year")
    author = author.title()
    journal = journal.title()
    author = author.strip()
    title = title.strip()
    journal = journal.strip()

    return author, title, journal, year, volume, number, pages, month, note

def generate_cite_key(author, year):
    '''Generate a cite key for a paper'''
    author = author.lower()
    return author.split(" ")[-1] + ":" + str(year)


def to_bibtex_article(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
    '''Convert a paper's information to bibtex format'''
    cite_key = generate_cite_key(author, year)
    res = "@article{" + cite_key + ",\n"
    input_str = read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
    #add to bibtext, handle empty fields with match case
    try:
        for i, value in enumerate(input_str):
            if i == 0 and value:
                res += f" author = {{{value}}},\n"
            elif i == 1 and value:
                res += f" title = {{{value}}},\n"
            elif i == 2 and value:
                res += f" journal = {{{value}}},\n"
            elif i == 3 and value:
                res += f" year = {{{value}}},\n"
            elif i == 4 and value:
                res += f" volume = {{{value}}},\n"
            elif i == 5 and value:
                res += f" number = {{{value}}},\n"
            elif i == 6 and value:
                res += f" pages = {{{value}}},\n"
            elif i == 7 and value:
                res += f" month = {{{value}}},\n"
            elif i == 8 and value:
                res += f" note = {{{value}}},\n"
        res += "}"
    except NameError:
        pass
    return res

def from_db_form_to_bibtex(article):
    author = article["author"]
    title = article["title"]
    journal = article["journal"]
    year = int(article["year"])
    if "volume" in article:
        volume = int(article["volume"])
    else:
        volume = 0
    if "number" in article:
        number = int(article["number"])
    else:
        number = 0
    if "pages" in article:
        pages = int(article["pages"])
    else:
        pages = 0
    if "month" in article:
        month = article["month"]
    else:
        month = ""
    if "note" in article:
        note = article["note"]
    else:
        note = ""
    bibtex_result = to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
    return bibtex_result

#author = "Matti Meikäläinen"
#title = "Tämä on otsikko"
#journal = "Journal of Journals"
#year = 2020
#volume = 1
#number = 2
#pages = 3
#month = 4
#note = "Tämä on huomautus"

#author, title, journal, year, volume, number, pages, month, note = read_user_input_article(author, title, journal, year, volume, number, pages)