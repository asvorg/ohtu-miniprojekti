'''Functions for handling article information'''
import datetime
from .book_func import to_bibtex_book
from .mastersthesis_func import to_bibtex_mastersthesis

def read_user_input_article(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
    '''Read user input and return a tuple of the paper's information'''
    if not author or not title or not journal or not year:
        raise ValueError("Author, title, journal and year are required fields")
    year = int(year)
    volume = int(volume)
    number = int(number)
    pages = pages
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
    if type(author) == list:
        author = author[0]
    author = author.lower()
    if len(author.split()) > 1:
        return author.split(" ")[1] + ":" + str(year)
    else:
        return author.split(" ")[0] + ":" + str(year)


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
        res = res[:-2]
        res += f"\n"
        res += "}"
    except NameError:
        pass
    return res

def from_db_form_to_bibtex(input_dict):
    '''Convert from db form to bibtex, for article, book and mastersthesis'''

    type = detect_type(input_dict)

    if type == "article":
        author = input_dict["author"]
        title = input_dict["title"]
        journal = input_dict["journal"]
        year = input_dict["year"]

        if "volume" in input_dict:
            volume = input_dict["volume"]
        else:
            volume = 0
        if "number" in input_dict:
            number = input_dict["number"]
        else:
            number = 0
        if "pages" in input_dict:
            pages = input_dict["pages"]
        else:
            pages = 0
        if "month" in input_dict:
            month = input_dict["month"]
        else:
            month = ""
        if "note" in input_dict:
            note = input_dict["note"]
        else:
            note = ""

        return to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)

    elif type == "book":
        author = input_dict["author"]
        editor = input_dict["editor"]
        title = input_dict["title"]
        publisher = input_dict["publisher"]
        year = input_dict["year"]

        if "volume" in input_dict:
            volume = input_dict["volume"]
        else:
            volume = 0
        if "number" in input_dict:
            number = input_dict["number"]
        else:
            number = 0
        if "series" in input_dict:
            series = input_dict["series"]
        else:
            series = ""
        if "address" in input_dict:
            address = input_dict["address"]
        else:
            address = ""
        if "edition" in input_dict:
            edition = input_dict["edition"]
        else:
            edition = ""
        if "month" in input_dict:
            month = input_dict["month"]
        else:
            month = ""
        if "note" in input_dict:
            note = input_dict["note"]
        else:
            note = ""
        if "doi" in input_dict:
            doi = input_dict["doi"]
        else:
            doi = ""
        if "issn" in input_dict:
            issn = input_dict["issn"]
        else:
            issn = ""
        if "isbn" in input_dict:
            isbn = input_dict["isbn"]
        else:
            isbn = ""

        return to_bibtex_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)

    elif type == "mastersthesis":
        author = input_dict["author"]
        title = input_dict["title"]
        school = input_dict["school"]
        year = input_dict["year"]

        if "type" in input_dict:
            type = input_dict["type"]
        else:
            type = ""
        if "address" in input_dict:
            address = input_dict["address"]
        else:
            address = ""
        if "month" in input_dict:
            month = input_dict["month"]
        else:
            month = ""
        if "note" in input_dict:
            note = input_dict["note"]
        else:
            note = ""
        if "annote" in input_dict:
            annote = input_dict["annote"]
        else:
            annote = ""

        return to_bibtex_mastersthesis(author, title, school, year, type, address, month, note, annote)



def detect_type(input_dict):
    '''Detect the type of the input'''
    if "journal" in input_dict:
        return "article"
    if "publisher" in input_dict:
        return "book"
    if "school" in input_dict:
        return "mastersthesis"
    return "misc"


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

generate_cite_key("Kääriäinen and Luukkainen", 2022)
