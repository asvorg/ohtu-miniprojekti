import unittest
#import sys
#sys.path.append("..")
from backend import article_func
from backend import book_func
from backend import crawl
from backend import mastersthesis_func
from backend.db import db_func
import pytest


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
    
    def test_detect_type(self):
        input_dict = {"author": "Matti Meikäläinen", "title": "Tämä on otsikko", "journal": "Journal of Journals", "year": 2020, "volume": 1, "number": 2, "pages": 3, "month": 4, "note": "Tämä on huomautus"}
        tulos = article_func.detect_type(input_dict)
        self.assertEqual(tulos, "article")

class TestDbFunc(unittest.TestCase):
    def setUp(self):
        pass
        #print("Set up goes here")

    def test_add_article_to_db(self):
        author = "Matti Pytest"
        title = "Tämä on otsikko"
        journal = "Journal of Journals"
        year = 2020
        volume = 1
        number = 2
        pages = 3
        month = 4
        note = "Tämä on huomautus"
        author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
        article = article_func.to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
        db_func.add_article_to_db("testiuser", article)
        tulos = db_func.get_article_from_db_by_cite_key("testiuser", "pytest:2020")
        self.assertEqual(tulos["author"], "Matti Pytest")
        self.assertEqual(tulos["title"], "Tämä on otsikko")
        self.assertEqual(tulos["journal"], "Journal Of Journals")
        self.assertEqual(tulos["year"], "2020")
        self.assertEqual(tulos["volume"], "1")
        self.assertEqual(tulos["number"], "2")
        self.assertEqual(tulos["pages"], "3")
        self.assertEqual(tulos["month"], "4")
        self.assertEqual(tulos["note"], "Tämä on huomautus")
        self.assertEqual(tulos["cite_key"], "pytest:2020")
        self.assertEqual(tulos["user"], "testiuser")
        db_func.delete_article_by_cite_key("testiuser", "pytest:2020")

    def test_get_article_from_db_by_cite_key(self):
        author = "Matti Pytest"
        title = "Tämä on otsikko"
        journal = "Journal of Journals"
        year = 2020
        volume = 1
        number = 2
        pages = 3
        month = 4
        note = "Tämä on huomautus"
        author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
        article = article_func.to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
        db_func.add_article_to_db("testiuser", article)
        tulos = db_func.get_article_from_db_by_cite_key("testiuser", "pytest:2020")
        self.assertEqual(tulos["author"], "Matti Pytest")
        self.assertEqual(tulos["title"], "Tämä on otsikko")
        self.assertEqual(tulos["journal"], "Journal Of Journals")
        self.assertEqual(tulos["year"], "2020")
        self.assertEqual(tulos["volume"], "1")
        self.assertEqual(tulos["number"], "2")
        self.assertEqual(tulos["pages"], "3")
        self.assertEqual(tulos["month"], "4")
        self.assertEqual(tulos["note"], "Tämä on huomautus")
        self.assertEqual(tulos["cite_key"], "pytest:2020")
        self.assertEqual(tulos["user"], "testiuser")
        db_func.delete_article_by_cite_key("testiuser", "pytest:2020")

    def test_get_articles_from_db_by_cite_key(self):
        author = "Matti Pytest"
        title = "Tämä on otsikko"
        journal = "Journal of Journals"
        year = 2020
        volume = 1
        number = 2
        pages = 3
        month = 4
        note = "Tämä on huomautus"
        author, title, journal, year, volume, number, pages, month, note = article_func.read_user_input_article(author, title, journal, year, volume, number, pages, month, note)
        article = article_func.to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)
        db_func.add_article_to_db("testiuser", article)
        lista = db_func.get_articles_from_db_by_cite_key("testiuser", "pytest:2020")
        tulos = lista[0]
        self.assertEqual(tulos["author"], "Matti Pytest")
        self.assertEqual(tulos["title"], "Tämä on otsikko")
        self.assertEqual(tulos["journal"], "Journal Of Journals")
        self.assertEqual(tulos["year"], "2020")
        self.assertEqual(tulos["volume"], "1")
        self.assertEqual(tulos["number"], "2")
        self.assertEqual(tulos["pages"], "3")
        self.assertEqual(tulos["month"], "4")
        self.assertEqual(tulos["note"], "Tämä on huomautus")
        self.assertEqual(tulos["cite_key"], "pytest:2020")
        self.assertEqual(tulos["user"], "testiuser")
        db_func.delete_article_by_cite_key("testiuser", "pytest:2020")

class TestBookFunc(unittest.TestCase):
    def setUp(self):
        pass
        #print("Set up goes here")

    def test_generate_cite_key(self):
        author = "Matti Meikäläinen"
        year = 2020
        tulos = book_func.generate_cite_key(author, year)
        self.assertEqual(tulos, "meikäläinen:2020")

    def test_to_bibtex_book(self):
        author = "Matti Meikäläinen"
        editor = "Matti Meikäläinen"
        title = "Tämä on otsikko"
        publisher = "Publisher of Publishers"
        year = 2020
        volume = 1
        number = 2
        series = 3
        address = 4
        edition = 5
        month = 6
        note = "Tämä on huomautus"
        doi = 7
        issn = 8
        isbn = 9
        author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn = book_func.read_user_input_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)
        tulos = book_func.to_bibtex_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)
        self.assertEqual(tulos, "@book{meikäläinen:2020,\n author = {Matti Meikäläinen},\n editor = {Matti Meikäläinen},\n title = {Tämä on otsikko},\n publisher = {Publisher Of Publishers},\n year = {2020},\n volume = {1},\n number = {2},\n series = {3},\n address = {4},\n edition = {5},\n month = {6},\n note = {Tämä on huomautus},\n doi = {7},\n issn = {8},\n isbn = {9},\n}")

class TestCrawl(unittest.TestCase):
    def setUp(self):
        pass
        #print("Set up goes here")

    def test_crawl_acm(self):

        title,journal,abstract,authors,published,pages,year = crawl.crawl_acm("https://dl.acm.org/doi/10.1145/2380552.2380613")
        self.assertEqual(title, "Three years of design-based research to reform a software engineering curriculum")
        self.assertEqual(journal, "Proceedings of the 13th annual conference on Information technology education")
        self.assertEqual(abstract, "Most of the research-oriented computer science departments provide software engineering education. Providing up-to-date software engineering education can be problematic, as practises used in modern software development companies have been developed in the industry and as such do not often reach teachers in university contexts. The danger, and often the unfortunate reality, is that institutions giving education in software engineering end up teaching the subject using outdated practices with technologies no longer in use. In this article we describe a three-year design-based research where the goal has been to design and reform a software engineering subtrack within our bachelor curriculum that would make it possible for the students to have strong up-to-date theoretical and practical skills in software engineering without a need to remove any of the existing theoretical aspects.")
        self.assertEqual(authors, ['Matti Luukkainen', 'Arto Vihavainen', 'Thomas Vikberg'])
        self.assertEqual(published, "11 October 2012")
        self.assertEqual(pages, "209–214")
        self.assertEqual(year, "2012")

        title,journal,abstract,authors,published,pages,year = crawl.crawl_acm("https://dl.acm.org/doi/10.4230/LIPIcs.CCC.2023.1")
        self.assertEqual(title, "Separation of the Factorization Norm and Randomized Communication Complexity")
        self.assertEqual(journal, "Proceedings of the conference on Proceedings of the 38th Computational Complexity Conference")
        self.assertEqual(authors,["Tsun-Ming Cheung","Hamed Hatami","Kaave Hosseini","Morgan Shirley"])

    def test_from_link_to_bibtex(self):
        tulos = crawl.from_link_to_bibtex("https://dl.acm.org/doi/10.1145/2380552.2380613")
        self.assertEqual(tulos, "@article{luukkainen:2012,\n author = {Matti Luukkainen and Arto Vihavainen and Thomas Vikberg},\n title = {Three years of design-based research to reform a software engineering curriculum},\n journal = {Proceedings of the 13th annual conference on Information technology education},\n year = {2012},\n pages = {209–214},\n}")


    def test_get_by_doi(self):
        title,journal,abstract,authors,published,pages,year = crawl.get_by_doi("10.1145/2380552.2380613")
        self.assertEqual(title, "Three years of design-based research to reform a software engineering curriculum")
        self.assertEqual(journal, "Proceedings of the 13th annual conference on Information technology education")
        self.assertEqual(abstract, "Most of the research-oriented computer science departments provide software engineering education. Providing up-to-date software engineering education can be problematic, as practises used in modern software development companies have been developed in the industry and as such do not often reach teachers in university contexts. The danger, and often the unfortunate reality, is that institutions giving education in software engineering end up teaching the subject using outdated practices with technologies no longer in use. In this article we describe a three-year design-based research where the goal has been to design and reform a software engineering subtrack within our bachelor curriculum that would make it possible for the students to have strong up-to-date theoretical and practical skills in software engineering without a need to remove any of the existing theoretical aspects.")
        self.assertEqual(authors, ['Matti Luukkainen', 'Arto Vihavainen', 'Thomas Vikberg'])
        self.assertEqual(published, "11 October 2012")
        self.assertEqual(pages, "209–214")
        self.assertEqual(year, "2012")

class TestMastersthesisFunc(unittest.TestCase):
    def setUp(self):
        pass
        #print("Set up goes here")

    def test_read_user_input_mastersthesis(self):
        with pytest.raises(ValueError):
            mastersthesis_func.read_user_input_mastersthesis("", "Title", "School", "2022", "", "", "", "", "")

        with pytest.raises(ValueError):
            mastersthesis_func.read_user_input_mastersthesis("Author", "Title", "School", "-1", "", "", "", "", "")

        input_data = mastersthesis_func.read_user_input_mastersthesis("Author", "Title", "School", "2022", "", "", "", "", "")
        assert input_data == ("Author", "Title", "School", 2022, "", "", "", "", "")

    def test_generate_cite_key(self):
        cite_key = mastersthesis_func.generate_cite_key("John Doe", 2022)
        assert cite_key == "doe:2022"

    def test_to_bibtex_mastersthesis(self):
        bibtex_entry = mastersthesis_func.to_bibtex_mastersthesis("John Doe", "Thesis Title", "University", "2022", "", "", "", "", "")
        expected_entry = (
            "@mastersthesis{doe:2022,\n"
            " author = {John Doe},\n"
            " title = {Thesis Title},\n"
            " school = {University},\n"
            " year = {2022},\n"
            "}"
        )
        assert bibtex_entry.strip() == expected_entry.strip()        

    if __name__ == '__main__':
        unittest.main()
