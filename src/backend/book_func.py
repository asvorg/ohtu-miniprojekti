'''Functions for related to adding book reference type'''
import datetime


def read_user_input_book(author, editor, title, publisher,year, volume, number, series, address, pages, month, note, doi, issn, isbn): #https://www.bibtex.com/e/book-entry/
    '''Read user input and return a tuple of the book's information'''
    if not author or not editor or not title or not publisher or not year:
        raise ValueError("Author, editor, title, publisher and year are required fields")
    year = int(year)
    volume = int(volume)
    number = int(number)
    
    if year < 0 or year > datetime.datetime.now().year:
        raise ValueError("Invalid year")
    author = author.title()
    editor = editor.title()
    title = title.title()
    publisher = publisher.title()
    author = author.strip()
    editor = editor.strip()
    title = title.strip()
    publisher = publisher.strip()

    return author, editor, title, publisher, year, volume, number, series, address, pages, month, note, doi, issn, isbn
    
def generate_cite_key(author, year):
    '''Generate a cite key for a book'''
    author = author.lower()
    return author.split(" ")[-1] + ":" + str(year)

def to_bibtex_book(author, editor, title, publisher, year, volume=0, number=0, series=0, address=0, edition=0, month=0, note="", doi=0, issn=0, isbn=0):
    '''Convert a book's information to bibtex format'''
    cite_key = generate_cite_key(author, year)
    res = "@book{" + cite_key + ",\n"
    input_str = read_user_input_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)
    #add to bibtext, handle empty fields with match case
    try:
        for i, value in enumerate(input_str):
            if i == 0 and value:
                res += f" author = {{{value}}},\n"
            elif i == 1 and value:
                res += f" editor = {{{value}}},\n"
            elif i == 2 and value:
                res += f" title = {{{value}}},\n"
            elif i == 3 and value:
                res += f" publisher = {{{value}}},\n"
            elif i == 4 and value:
                res += f" year = {{{value}}},\n"
            elif i == 5 and value:
                res += f" volume = {{{value}}},\n"
            elif i == 6 and value:
                res += f" number = {{{value}}},\n"
            elif i == 7 and value:
                res += f" series = {{{value}}},\n"
            elif i == 8 and value:
                res += f" address = {{{value}}},\n"
            elif i == 9 and value:
                res += f" edition = {{{value}}},\n"
            elif i == 10 and value:
                res += f" month = {{{value}}},\n"
            elif i == 11 and value:
                res += f" note = {{{value}}},\n"
            elif i == 12 and value:
                res += f" doi = {{{value}}},\n"
            elif i == 13 and value:
                res += f" issn = {{{value}}},\n"
            elif i == 14 and value:
                res += f" isbn = {{{value}}},\n"
        res += "}"
    except NameError:
        pass
    return res

def to_bibtex_book(author, editor, title, publisher, year, volume=0, number=0, series=0, address=0, edition=0, month=0, note="", doi=0, issn=0, isbn=0):
    '''Convert a book's information to bibtex format'''
    cite_key = generate_cite_key(author, year)
    res = "@book{" + cite_key + ",\n"
    input_str = read_user_input_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)
    #add to bibtext, handle empty fields with match case
    try:
        for i, value in enumerate(input_str):
            if i == 0 and value:
                res += f" author = {{{value}}},\n"
            elif i == 1 and value:
                res += f" editor = {{{value}}},\n"
            elif i == 2 and value:
                res += f" title = {{{value}}},\n"
            elif i == 3 and value:
                res += f" publisher = {{{value}}},\n"
            elif i == 4 and value:
                res += f" year = {{{value}}},\n"
            elif i == 5 and value:
                res += f" volume = {{{value}}},\n"
            elif i == 6 and value:
                res += f" number = {{{value}}},\n"
            elif i == 7 and value:
                res += f" series = {{{value}}},\n"
            elif i == 8 and value:
                res += f" address = {{{value}}},\n"
            elif i == 9 and value:
                res += f" edition = {{{value}}},\n"
            elif i == 10 and value:
                res += f" month = {{{value}}},\n"
            elif i == 11 and value:
                res += f" note = {{{value}}},\n"
            elif i == 12 and value:
                res += f" doi = {{{value}}},\n"
            elif i == 13 and value:
                res += f" issn = {{{value}}},\n"
            elif i == 14 and value:
                res += f" isbn = {{{value}}},\n"
        res += "}"
    except NameError:
        pass
    return res