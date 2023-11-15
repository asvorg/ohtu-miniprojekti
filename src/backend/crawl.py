import requests


def crawl(url):
    return requests.get(url).text

print(crawl("https://dl.acm.org/doi/10.1145/2380552.2380613"))