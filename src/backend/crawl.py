import requests
from datetime import datetime
from backend import article_func

def crawl_acm(url):
    '''Crawl a paper from ACM'''
    text = requests.get(url).text
    title = text.split("<title>")[1].split("</title>")[0]
    abstract = text.split("<div class=\"abstractSection abstractInFull\">")[1].split("</div>")[0]
    #clean the abstract
    abstract = abstract.replace("<p>", "")
    abstract = abstract.replace("</p>", "")
    abstract = abstract.replace("\n","")
    abstract = abstract.replace("\t","")

    journal = title.split("|")[1]
    journal = journal.strip()

    title = title.split("|")[0]
    title = title.strip()

    authors = text.split("Authors:")[1].split("/></a></div>")[0]
    authors = authors.split("aria-hidden=\"true\"/>")[1:]

    for i in range(len(authors)):
        authors[i] = authors[i].split("</span>")[0]
        authors[i] = authors[i].strip()

    published = text.split("<span class=\"CitationCoverDate\">")[1].split("</span>")[0]

    pages = text.split("<span class=\"epub-section__pagerange\">")[1].split("</span>")[0]
    pages = pages.replace("Pages ", "")
    pages = pages.strip()
    year = published.split(" ")[-1]


    return title, journal, abstract, authors, published, pages, year

def get_by_doi(doi):
    '''Get a paper by doi'''    
    url = "https://dl.acm.org/doi/" + doi
    return crawl_acm(url)


def acm_to_bibtex(author, title, journal, year, volume=0, number=0, pages=0, month=0, note=""):
    cite_key = article_func.generate_cite_key(author, year)
    pages = pages.split("-")[0]
    res = "@article{" + cite_key + ",\n"
    author_cp = ""
    if type(author) == list:
        for i in author:
            author_cp += i + " and "
        #remove the last " and "
        author_cp = author_cp[:-5]
    input_str = author_cp, title, journal, year, volume, number, pages, month, note
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

def from_link_to_bibtex(link):
    '''Get a paper from a link and return a bibtex'''

    title, journal, abstract, authors, published, pages, year = crawl_acm(link)
    return acm_to_bibtex(authors, title, journal, year, pages=pages)


#title,journal,abstract,authors,published,pages,year = crawl_acm("https://dl.acm.org/doi/10.1145/2380552.2380613")
#print(acm_to_bibtex(authors, title, journal, year, pages=pages))


#get references as a list
#references = text.split("<li class=\"references__item\">")
#split refnces by line
#for i in range(len(references)):
#    references[i] = references[i].split("\n")
