from flask import Flask
from flask import render_template, request
from backend.article_func import to_bibtex_article
from backend.db.db_func import add_article_to_db

app = Flask(__name__, template_folder='frontend/templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        user = request.form["Käyttäjä"]
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
        add_article_to_db(user, bibtex_result)
        
        return render_template("result.html", bibtex_result=bibtex_result, user = user)

    except ValueError as e:
        return render_template("error.html", error_message=str(e))

@app.route("/list/")
def list():
    #kesken!

    viitteet = [{"id": 123, "author": "ville.vallaton", "title": "Otsikkoinen"}, {"id": 321, "author": "ville.vallatonfdsfds", "title": "Otsikkoinen"}]
    return render_template("list.html", viitteet=viitteet)

@app.route("/edit/<int:viite_id>/")
def edit(viite_id):
    return render_template("edit.html")

@app.route("/delete/<int:viite_id>/")
def delete(viite_id):
    return render_template("delete.html")
