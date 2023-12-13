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
    if isinstance(author, list):
        author = author[0]
    author = author.lower()
    if len(author.split()) > 1:
        return author.split(" ")[1] + ":" + str(year)
    return author.split(" ")[0] + ":" + str(year)


def to_bibtex_article(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
    '''Convert a paper's information to BibTeX format'''

    cite_key = generate_cite_key(author, year)
    res = f"@article{{{cite_key},\n"
    input_str = read_user_input_article(author, title, journal, year, volume, number, pages, month, note)

    try:
        for i, value in enumerate(input_str):
            if value:
                field_names = ["author", "title", "journal", "year", "volume", "number", "pages", "month", "note"]
                res += f" {field_names[i]} = {{{value}}},\n"
        res = res[:-2]
        res += f"\n}}"
    except NameError:
        pass

    return res


def from_db_form_to_bibtex(input_dict):
    '''Convert from db form to BibTeX, for article, book, and mastersthesis'''

    type = detect_type(input_dict)

    if type == "article":
        author = input_dict.get("author", "")
        title = input_dict.get("title", "")
        journal = input_dict.get("journal", "")
        year = input_dict.get("year", "")
        volume = input_dict.get("volume", 0)
        number = input_dict.get("number", 0)
        pages = input_dict.get("pages", 0)
        month = input_dict.get("month", "")
        note = input_dict.get("note", "")

        return to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)

    if type == "book":
        author = input_dict.get("author", "")
        editor = input_dict.get("editor", "")
        title = input_dict.get("title", "")
        publisher = input_dict.get("publisher", "")
        year = input_dict.get("year", "")
        volume = input_dict.get("volume", 0)
        number = input_dict.get("number", 0)
        series = input_dict.get("series", "")
        address = input_dict.get("address", "")
        edition = input_dict.get("edition", "")
        month = input_dict.get("month", "")
        note = input_dict.get("note", "")
        doi = input_dict.get("doi", "")
        issn = input_dict.get("issn", "")
        isbn = input_dict.get("isbn", "")

        return to_bibtex_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)

    if type == "mastersthesis":
        author = input_dict.get("author", "")
        title = input_dict.get("title", "")
        school = input_dict.get("school", "")
        year = input_dict.get("year", "")
        type = input_dict.get("type", "")
        address = input_dict.get("address", "")
        month = input_dict.get("month", "")
        note = input_dict.get("note", "")
        annote = input_dict.get("annote", "")

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
