import requests


def crawl_acm(url):
    '''''''''''
    Crawl the abstract and references of a paper from ACM Digital Library
    '''''''''''
    #get the html text
    text = requests.get(url).text
    #keep only the text in div with class 'abstractSection abstractInFull'
    abstract = text[text.find('<div class="abstractSection abstractInFull">'):]
    #keep only the first paragraph
    abstract = abstract[abstract.find('<p>')+3:abstract.find('</p>')]
    #get references
    references = text[text.find('<ol class="rlist references__list references__numeric">'):]
    #get all span class= "references__note"
    references = references.split('<span class="references__note">')

    return references

print(crawl_acm("https://dl.acm.org/doi/10.1145/2380552.2380613"))