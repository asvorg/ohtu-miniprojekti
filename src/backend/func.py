import datetime


def read_user_input(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
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
    title = title.title()
    journal = journal.title()
    author = author.strip()
    title = title.strip()
    journal = journal.strip()

    return author, title, journal, year, volume, number, pages, month, note

def generate_cite_key(author, year):
    '''Generate a cite key for a paper'''
    author = author.lower()
    return author.split(" ")[-1] + ":" + str(year)

    

def to_bibtex(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""): #ei valmis
    '''Convert a paper's information to bibtex format'''
    cite_key = generate_cite_key(author, year)




