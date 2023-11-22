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
        article_name = request.form["ArtikkelinNimi"]
        year = request.form["Julkaisuvuosi"]

        bibtex_result = to_bibtex_article(author, title, article_name, year)

        return render_template("result.html", article_name=article_name, bibtex_result=bibtex_result)

    except ValueError as e:
        return render_template("error.html", error_message=str(e))

@app.route("/list")
def list():
    #kesken!

    viitteet = [{"author": "ville.vallaton", "title": "Otsikkoinen"}, {"author": "ville.vallatonfdsfds", "title": "Otsikkoinen"}]
    return render_template("list.html", viitteet=viitteet)
