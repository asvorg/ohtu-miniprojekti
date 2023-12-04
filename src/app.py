from flask import Flask
from flask import render_template, request, redirect, url_for, session, send_file
from backend.article_func import to_bibtex_article, from_db_form_to_bibtex, detect_type
from backend.db.db_func import add_article_to_db, get_article_from_db_by_user, add_mastersthesis_to_db, delete_article_by_cite_key, get_article_from_db_by_cite_key, add_book_to_db, get_articles_from_db_by_cite_key, get_articles_from_db_by_tag
from backend.book_func import to_bibtex_book
from backend.mastersthesis_func import to_bibtex_mastersthesis
from backend.crawl import crawl_acm, from_link_to_bibtex

app = Flask(__name__, template_folder='frontend/templates')
app.secret_key = '9876543dd'

@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username

        return redirect(url_for("result_by_user", user = username))

    return render_template("signin.html")

@app.route("/result/<user>/")
def result_by_user(user):
    articles = get_article_from_db_by_user(user)

    article = []
    for a in articles:
        bib_res = from_db_form_to_bibtex(a)
        article.append(bib_res)

    return render_template("result.html", user=user, articles=article)

@app.route("/add_article/<user>/")
def add_article(user):
    user = session.get("username")
    return render_template("index.html", user=user)

@app.route("/result_article/<user>/", methods=["POST"])
def result_article(user):
    try:
        user = session.get("username")
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

        return redirect(url_for("result_by_user", user=user))

    except ValueError as e:
        return render_template("index.html", error_message=str(e), user=user)

@app.route("/add_book/<user>/")
def add_book(user):
    user = session.get("username")
    return render_template("book.html", user=user)

@app.route("/result_book/<user>/", methods=["POST"])
def result_book(user):
    try:
        user = session.get("username")
        author = request.form["Kirjoittaja"]
        editor = request.form["Editori"]
        title = request.form["Otsikko"]
        publisher = request.form["Julkaisija"]
        year = int(request.form["Julkaisuvuosi"])

        volume = int(request.form["Vuosikerta"]) if request.form["Vuosikerta"] else 0
        number = int(request.form["Numero"]) if request.form["Numero"] else 0
        pages = int(request.form["Sivumäärä"]) if request.form["Sivumäärä"] else 0
        month = request.form["Kuukausi"]
        series = request.form["Sarja"]
        address = request.form["Osoite"]
        note = request.form["Huomautus"]
        doi = request.form["Doi"]
        issn = request.form["Issn"]
        isbn = request.form["Isbn"]

        bibtex_book = to_bibtex_book(author, editor, title, publisher, year, volume, number, series, address, pages, month, note, doi, issn, isbn)

        add_book_to_db(user, bibtex_book)

        return redirect(url_for("result_by_user", user=user))

    except ValueError as e:
        return render_template("book.html", error_message=str(e), user=user)

@app.route("/add_mastersthesis/<user>/")
def add_mastersthesis(user):
    user = session.get("username")
    return render_template("mastersthesis.html", user=user)

@app.route("/result_mastersthesis/<user>/", methods=["POST"])
def result_mastersthesis(user):
    try:
        user = session.get("username")
        author = request.form["Kirjoittaja"]
        title = request.form["Otsikko"]
        school = request.form["Koulu"]
        year = int(request.form["Julkaisuvuosi"])

        type = request.form["Tyyppi"]
        address = request.form["Osoite"]
        month = request.form["Kuukausi"]
        note = request.form["Huomautus"]
        annote = request.form["Kommentti"]

        bibtex_mastersthesis = to_bibtex_mastersthesis(author, title, school, year, type, address, month, note, annote)

        add_mastersthesis_to_db(user, bibtex_mastersthesis)

        return redirect(url_for("result_by_user", user=user))

    except ValueError as e:
        return render_template("mastersthesis.html", error_message=str(e), user=user)

@app.route("/add_acm/<user>/")
def add_acm(user):
    user = session.get("username")
    return render_template("acm.html", user=user)


# AAPO TÄÄLLLÄÄ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route("/result_acm/<user>/", methods=["POST"])
def result_acm(user):
    try:
        user = session.get("username")
        add_link = request.form["Linkki"]

        acm_link = crawl_acm(add_link)

        bibtex_acm_link = from_link_to_bibtex(acm_link)

        return render_template("testi.html", bibtex_acm_link=bibtex_acm_link, user=user)

        #return redirect(url_for("result_by_user", user=user))
    
    except ValueError as e:
        return render_template("testi.html", e=str(e))

@app.route("/search/<user>/", methods=["POST"])
def search_result_by_cite_key(user):
    try:
        cite_key = request.form["Avain"]
        get_references = get_articles_from_db_by_cite_key(user, cite_key)
        references = []
        for reference in get_references:
            bib_res = from_db_form_to_bibtex(reference)
            references.append(bib_res)
        return render_template("search.html", user=user, cite_key=cite_key, references=references)
    except Exception as e:
        return render_template("result.html", user=user, error_message=str(e))

@app.route("/search/<user>/tag/", methods=["POST"])
def search_result_by_tag(user):
    try:
        tag = request.form["Tagi"]
        get_references = get_articles_from_db_by_tag(user, tag)
        references = []
        for reference in get_references:
            bib_res = from_db_form_to_bibtex(reference)
            references.append(bib_res)
        return render_template("search.html", user=user, tag=tag, references=references)
    except Exception as e:
        return render_template("result.html", user=user, error_message=str(e))

@app.route("/list/")
def list_without_user():
    return "Kirjoita käyttäjän nimi osoitteen loppuun: .../list/<käyttäjän nimi>"

@app.route("/list/<user>/")
def list(user):
    cites = get_article_from_db_by_user(user)
    cite_types = {}
    for cite in cites:
        cite_types[cite["cite_key"]] = detect_type(cite)
    return render_template("list.html", cites=cites, user=user, cite_types=cite_types)

@app.route("/list/<user>/tag/<tag>/")
def list_by_tag(user, tag):
    cites = get_articles_from_db_by_tag(user, tag=tag)
    cite_types = {}
    for cite in cites:
        cite_types[cite["cite_key"]] = detect_type(cite)
    return render_template("list.html", cites=cites, user=user, cite_types=cite_types)

@app.route("/edit/<user>/<cite_key>/", methods=["GET", "POST"])
def edit(user, cite_key):
    if request.method == "GET":
        cite = get_article_from_db_by_cite_key(user, cite_key)
        return render_template("edit.html", cite=cite)
    if request.method == "POST":
        # poisto
        delete_article_by_cite_key(user, cite_key)

        # lisäys
        user = session.get("username")
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
        tags = request.form["Tagit"]
        if len(tags) > 0:
            tags = tags.replace(" ", "").split(",")
        else:
            tags = None
        add_article_to_db(user, bibtex_result, tags)

        return redirect("/list/"+user)

@app.route("/edit_book/<user>/<cite_key>/", methods=["GET", "POST"])
def edit_book(user, cite_key):
    if request.method == "GET":
        cite = get_article_from_db_by_cite_key(user, cite_key)
        return render_template("edit_book.html", cite=cite, user=user)
    if request.method == "POST":
        # poisto
        delete_article_by_cite_key(user, cite_key)

        # kirjaviitteen lisäys
        author = request.form["Kirjoittaja"]
        editor = request.form["Editori"]
        title = request.form["Otsikko"]
        publisher = request.form["Julkaisija"]
        year = int(request.form["Julkaisuvuosi"])
        volume = int(request.form["Vuosikerta"]) if request.form["Vuosikerta"] else 0
        number = int(request.form["Numero"]) if request.form["Numero"] else 0
        #pages = int(request.form["Sivumäärä"]) if request.form["Sivumäärä"] else 0 # pages ei tallennu tietokantaan!?
        month = request.form["Kuukausi"]
        series = request.form["Sarja"]
        address = request.form["Osoite"]
        note = request.form["Huomautus"]
        doi = request.form["Doi"]
        issn = request.form["Issn"]
        isbn = request.form["Isbn"]
        edition = "" # halutaanko edition myös lomakkeelle?!
        tags = request.form["Tagit"]
        if len(tags) > 0:
            tags = tags.replace(" ", "").split(",")
        else:
            tags = None
        bibtex_book = to_bibtex_book(author, editor, title, publisher, year, volume, number, series, address, edition, month, note, doi, issn, isbn)
        add_book_to_db(user, bibtex_book, tags)

        return redirect("/list/"+user)

@app.route("/edit_mastersthesis/<user>/<cite_key>/", methods=["GET", "POST"])
def edit_mastersthesis(user, cite_key):
    if request.method == "GET":
        cite = get_article_from_db_by_cite_key(user, cite_key)
        return render_template("edit_mastersthesis.html", cite=cite)
    if request.method == "POST":
        # poisto ja lisäys
        delete_article_by_cite_key(user, cite_key)
        author = request.form["Kirjoittaja"]
        title = request.form["Otsikko"]
        school = request.form["Koulu"]
        year = int(request.form["Julkaisuvuosi"])
        type = request.form["Tyyppi"]
        address = request.form["Osoite"]
        month = request.form["Kuukausi"]
        note = request.form["Huomautus"]
        annote = request.form["Kommentti"]
        tags = request.form["Tagit"]
        if len(tags) > 0:
            tags = tags.replace(" ", "").split(",")
        else:
            tags = None
        bibtex_mastersthesis = to_bibtex_mastersthesis(author, title, school, year, type, address, month, note, annote)
        add_mastersthesis_to_db(user, bibtex_mastersthesis, tags)

        return redirect("/list/"+user)

@app.route("/delete/<user>/<cite_key>/", methods=["GET", "POST"])
def delete(user, cite_key):
    cite = get_article_from_db_by_cite_key(user, cite_key)
    # varmistuskysymys
    if request.method == "GET":
        bibtex = from_db_form_to_bibtex(cite)
        return render_template("delete_confirmation.html", user=user, cite_key=cite_key, bibtex=bibtex)
    # poisto
    if request.method == "POST":
        delete_article_by_cite_key(user, cite_key)
        return render_template("deleted.html", user=user)

@app.route("/download_bibtex/")
def download_bibtex_file():
    if not session.get("username"):
        return "Et ole kirjautunut."
    
    user = session["username"]

    articles = get_article_from_db_by_user(user)
    article = []
    for a in articles:
        bib_res = from_db_form_to_bibtex(a)
        article.append(bib_res)

    filename = "bibtex.bib"
    file = open(filename, "w") # tiedosto src-kansioon, jos ei vielä ole
    file.write("\n\n".join(article))
    file.close()

    return send_file(filename, as_attachment=True)
 