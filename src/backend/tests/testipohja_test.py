import unittest
from crawl import crawl_acm
import article_func


#class TestCrawlAcm(unittest.TestCase):
#    def setUp(self):
#        pass
#        #print("Set up goes here")

class TestArticleFunc(unittest.TestCase):
    def setUp(self):
        pass
        #print("Set up goes here")

    def test_generate_cite_key(self):
        
        author = "Matti Meikäläinen"
        year = 2020
        tulos = article_func.generate_cite_key(author, year)
        self.assertEqual(tulos, "meikäläinen:2020")
    
    def test_to_bibtex_article(self):
        author = "Matti Meikäläinen"
        title = "Tämä on otsikko"
        journal = "Journal of Journals"
        year = 2020
        volume = 1
        number = 2
        pages = 3
        month = 4
        note = "Tämä on huomautus"
        author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
        tulos = article_func.to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
        self.assertEqual(tulos, "@article{meikäläinen:2020,\n author = {Matti Meikäläinen},\n title = {Tämä on otsikko},\n journal = {Journal Of Journals},\n year = {2020},\n volume = {1},\n number = {2},\n pages = {3},\n month = {4},\n note = {Tämä on huomautus},\n}")

    def test_read_user_input_article(self):
        author = "Matti Meikäläinen"
        title = "Tämä on otsikko"
        journal = "Journal of Journals"
        year = 2020
        volume = 1
        number = 2
        pages = 3
        month = 4
        note = "Tämä on huomautus"
        author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
        self.assertEqual(author, "Matti Meikäläinen")
        self.assertEqual(title, "Tämä on otsikko")
        self.assertEqual(journal, "Journal Of Journals")
        self.assertEqual(year, 2020)
        self.assertEqual(volume, 1)
        self.assertEqual(number, 2)
        self.assertEqual(pages, 3)
        self.assertEqual(month, 4)
        self.assertEqual(note, "Tämä on huomautus")

    if __name__ == '__main__':
        unittest.main()
