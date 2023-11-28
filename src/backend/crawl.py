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

    authors = text.split("Authors:")[1].split("/></a></div>")[0]
    authors = authors.split("aria-hidden=\"true\"/>")[1:]
    
    for i in range(len(authors)):
        authors[i] = authors[i].split("</span>")[0]
        authors[i] = authors[i].strip()
    
    published = text.split("<span class=\"CitationCoverDate\">")[1].split("</span>")[0]

    pages = text.split("<span class=\"epub-section__pagerange\">")[1].split("</span>")[0]
    pages = pages.replace("Pages ", "")
    pages = pages.strip()
    
    return title, abstract, authors, published, pages

print(crawl_acm("https://dl.acm.org/doi/10.1145/2380552.2380613"))


#get references as a list
#references = text.split("<li class=\"references__item\">")
#split refnces by line
#for i in range(len(references)):
#    references[i] = references[i].split("\n")