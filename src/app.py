from flask import Flask
from flask import render_template, request
from backend.article_func import read_user_input_article, to_bibtex_article


app = Flask(__name__, template_folder='frontend/templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        author = request.form["Kirjoittaja"]
        title = request.form["Otsikko"]
        journal = request.form["Artikkeli"]
        year = int(request.form["Julkaisuvuosi"])

        volume = int(request.form["Vuosikerta"]) if request.form["Vuosikerta"] else 0
        number = int(request.form["Numero"]) if request.form["Numero"] else 0
        pages = int(request.form["Sivumäärä"]) if request.form["Sivumäärä"] else 0
        month = request.form["Kuukausi"]
        note = request.form["Huomautus"]

        bibtex_result = to_bibtex_article(author, title, journal, year, volume, number, pages, month, note)

        return render_template("result.html", bibtex_result=bibtex_result)

    except ValueError as e:
        return render_template("error.html", error_message=str(e))

@app.route("/list")
def list():
    #kesken!

    viitteet = [{"author": "ville.vallaton", "title": "Otsikkoinen"}, {"author": "ville.vallatonfdsfds", "title": "Otsikkoinen"}]
    return render_template("list.html", viitteet=viitteet)
