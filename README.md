![GHA workflow badge](https://github.com/asvorg/ohtu-miniprojekti/workflows/CI/badge.svg)

# ohtu-miniprojekti

[Linkki Backlogiin](https://docs.google.com/spreadsheets/d/16oLOVjyAvzNTiq1DqT4437QIkMCs-a8WFKWrO-61xKg/edit?usp=sharing)

[Linkki testikattavuusraporttiin](file:///home/anessina/ohtu-miniprojekti/htmlcov/index.html)

Definition of done = "Vaatimus on analysoitu, suunniteltu, ohjelmoitu, testattu, testaus automatisoitu, dokumentoitu, integroitu muuhun ohjelmistoon ja viety tuotantoympäristöön."

# Käynnistysohjeet
- Kloonaa repositorio koneellesi ja siirry sen juurikansioon
- Luo Pythonin virtuaaliympäristö kansion sisään komennolla python3 -m venv venv
- Aktivoi virtuaaliympäristö: poetry shell
- Asenna riippuvuudet: poetry install
- Siirry kansioon src
- Käynnistä sovellus: flask run
