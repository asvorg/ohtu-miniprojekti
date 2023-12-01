'''Functions for related to adding book reference type'''
import datetime



def read_user_input_masterthesis(author, title, school, year, type, address, month, note, annote):
    '''Read user input and return a tuple of the book's information'''
    if not author or not title or not school or not year:
        raise ValueError("Author, title, school and year are required fields")
    year = int(year)
    if year < 0 or year > datetime.datetime.now().year:
        raise ValueError("Invalid year")
    author = author.strip()
    title = title.strip()
    school = school.strip()
    year = year.strip()
    type = type.strip()
    address = address.strip()
    month = month.strip()
    note = note.strip()
    annote = annote.strip()

    return author, title, school, year, type, address, month, note, annote  
    
def generate_cite_key(author, year):
    '''Generate a cite key for a book'''
    author = author.lower()
    return author.split(" ")[-1] + ":" + str(year)

def to_bibtex_masterthesis(author, title, school, year, type, address, month, note, annote):
    '''Convert a book's information to bibtex format'''
    cite_key = generate_cite_key(author, year)
    res = "@masterthesis{" + cite_key + ",\n"
    input_str = read_user_input_masterthesis(author, title, school, year, type, address, month, note, annote)
    #add to bibtext, handle empty fields with match case
    try:
        for i, value in enumerate(input_str):
            if i == 0 and value:
                res += f" author = {{{value}}},\n"
            elif i == 1 and value:
                res += f" title = {{{value}}},\n"
            elif i == 2 and value:
                res += f" school = {{{value}}},\n"
            elif i == 3 and value:
                res += f" year = {{{value}}},\n"
            elif i == 4 and value:
                res += f" type = {{{value}}},\n"
            elif i == 5 and value:
                res += f" address = {{{value}}},\n"
            elif i == 6 and value:
                res += f" month = {{{value}}},\n"
            elif i == 7 and value:
                res += f" note = {{{value}}},\n"
            elif i == 8 and value:
                res += f" annote = {{{value}}},\n"
        res += "}"
    except NameError:
        pass
    return res

