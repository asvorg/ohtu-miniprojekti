![GHA workflow badge](https://github.com/asvorg/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/asvorg/ohtu-miniprojekti/graph/badge.svg?token=TDI48PGLLQ)](https://codecov.io/gh/asvorg/ohtu-miniprojekti)

# Viitteiden tallennussovellus

Tällä sovelluksella voit tallentaa erilaisia viitteitä bibtex-muodossa, kuten artikkeli-, kirja-, gradu- tai acm-linkkimuodossa. Viitteitä pystyy tarkastelemaan, muokkaamaan tai poistamaan.

[Linkki Backlogiin](https://docs.google.com/spreadsheets/d/16oLOVjyAvzNTiq1DqT4437QIkMCs-a8WFKWrO-61xKg/edit?usp=sharing)

[Linkki testikattavuusraporttin](https://app.codecov.io/gh/asvorg/ohtu-miniprojekti/tree/main/src%2Fbackend)

[Linkki CI-palveluun](https://github.com/asvorg/ohtu-miniprojekti/actions)

Definition of done = "Vaatimus on analysoitu, suunniteltu, ohjelmoitu, testattu, testaus automatisoitu, dokumentoitu, integroitu muuhun ohjelmistoon ja viety tuotantoympäristöön."

## Käynnistysohjeet
- Kloonaa repositorio koneellesi ja siirry sen juurikansioon
- Asenna riippuvuudet: poetry install
- Aktivoi virtuaaliympäristö: poetry shell
- Siirry kansioon src
- Käynnistä sovellus: flask run

## Testit
Komento virtuaaliympäristössä:
```
 pytest
```


## Pylint-tarkistukset
Komento juurihakemistosta:
```
pylint src
```
## Coverage
Yksikkötestit saa ajettua komennolla juurihakemistossa:

```bash
poetry run coverage run --branch -m pytest src
```
Testikattavuusraportin saa:

```bash
poetry run coverage html
```
Komentoriville testikattavuusraportin saa:

```bash
poetry run coverage report -m
