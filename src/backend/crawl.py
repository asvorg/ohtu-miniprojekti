import requests
from datetime import datetime


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
    
    return title, journal, abstract, authors, published, pages

def get_by_doi(doi):
    '''Get a paper by doi'''
    url = "https://dl.acm.org/doi/" + doi
    return crawl_acm(url)


title,journal, abstract, authors, published, pages = crawl_acm("https://dl.acm.org/doi/10.1145/2380552.2380613")
print("Title: ", title)
print("Journal: ", journal)
print("Abstract: ", abstract)
print("Authors: ", authors)
print("Published: ", published)
print("Pages: ", pages)

#get references as a list
#references = text.split("<li class=\"references__item\">")
#split refnces by line
#for i in range(len(references)):
#    references[i] = references[i].split("\n")