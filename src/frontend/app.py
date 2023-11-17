from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", a=request.form["Kirjoittaja"], b=request.form["Otsikko"], c=request.form["Julkaisuvuosi"], d=request.form["Artikkelin nimi"])