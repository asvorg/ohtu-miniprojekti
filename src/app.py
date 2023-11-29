from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session
from backend.article_func import to_bibtex_article,  from_db_form_to_bibtex
from backend.db.db_func import add_article_to_db, get_article_from_db_by_user, delete_article_by_cite_key, get_article_from_db_by_cite_key, edit_article_by_cite_key


app = Flask(__name__, template_folder='frontend/templates')
app.secret_key = '9876543dd' 

@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username

        return redirect(url_for("index"))

    return render_template("signin.html")


@app.route("/index")
def index():
    username = session.get("username", "Vieras") 
    return render_template("index.html", username=username)

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

        articles = get_article_from_db_by_user(user)
        article = []
        for a in articles:
            bib_res = from_db_form_to_bibtex(a)
            article.append(bib_res)

        return render_template("result.html", user=user, article=article)
            
    except ValueError as e:
        return render_template("index.html", error_message=str(e))

@app.route("/result/<user>/")
def result_by_user(user):
    #article = get_article_from_db_by_user(user)
    articles = get_article_from_db_by_user(user)
    article = []
    for a in articles:
        bib_res = from_db_form_to_bibtex(a)
        article.append(bib_res)
    return render_template("result.html", user=user, article=article)

@app.route("/search/<user>/", methods=["POST"])
def search_result_by_cite_key(user):
    try:
        cite_key = request.form["Avain"]
        articles = get_article_from_db_by_cite_key(user, cite_key)
        print(articles)
        article = []
        for a in articles:
            bib_res = from_db_form_to_bibtex(a)
            article.append(bib_res)
        print(article)
        return render_template("result.html", user=user, article=article)
    except Exception as e:
        return render_template("result.html", user=user, error_message=str(e))


@app.route("/list/")
def list_without_user():
    return "Kirjoita käyttäjän nimi osoitteen loppuun: .../list/<käyttäjän nimi>"

@app.route("/list/<user>")
def list(user):
    cites = get_article_from_db_by_user(user)
    return render_template("list.html", cites=cites, user=user)

@app.route("/edit/<user>/<cite_key>/", methods=["GET", "POST"])
def edit(user, cite_key):
    if request.method == "GET":
        cite = get_article_from_db_by_cite_key(user, cite_key)
        return render_template("edit.html", cite=cite)
    if request.method == "POST":
        # poisto
        delete_article_by_cite_key(user, cite_key)

        # lisäys
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
    
        cites = get_article_from_db_by_user(user)

        return redirect("/list/"+user)

@app.route("/delete/<user>/<cite_key>/", methods=["GET", "POST"])
def delete(user, cite_key):
    cite = get_article_from_db_by_cite_key(user, cite_key)
    # vahvistus
    if request.method == "GET":
        bibtex = from_db_form_to_bibtex(cite)
        return render_template("delete_confirmation.html", user=user, cite_key=cite_key, bibtex=bibtex)
    # poisto
    if request.method == "POST":
        delete_article_by_cite_key(user, cite_key)
        return render_template("deleted.html", user=user)
