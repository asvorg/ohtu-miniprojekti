from flask import Flask
from flask import render_template, request


app = Flask(__name__, template_folder='frontend/templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", author=request.form["Kirjoittaja"], title=request.form["Otsikko"], year=request.form["Julkaisuvuosi"], article_name=request.form["ArtikkelinNimi"])

@app.route("/list")
def list():
    #kesken!

    viitteet = [{"author": "ville.vallaton", "title": "Otsikkoinen"}, {"author": "ville.vallatonfdsfds", "title": "Otsikkoinen"}]
    return render_template("list.html", viitteet=viitteet)
