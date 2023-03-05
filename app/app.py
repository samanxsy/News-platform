import os
import requests
from flask import Flask, render_template, request


app = Flask("YourO News", static_folder='./app/static', template_folder='./app/templates')
newsAPI_KEY = os.environ.get('newsAPI_KEY')
app.config['SECRET_KEY'] = os.environ.get('SESSION_KEY')


@app.route("/")
def home():
    """This function will return the home page where the user can search about any topic"""
    search = request.args.get('search')
    if search:
        search = search.replace(" ", "+")

    url = f"https://newsapi.org/v2/everything?q={search}&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route("/search")
def search():
    """This function will return the content user searched for"""
    search = request.args.get('search')
    if search:
        search = search.replace(" ", "+")

    url = f"https://newsapi.org/v2/everything?q={search}&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route("/health")
def health():
    """This function will return top health headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=health&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route('/technology', methods=["GET"])
def technology():
    """This function will return top technology headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=technology&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route("/business")
def business():
    """
    This function will return top business headlines from US, UK and Hungary
    """
    # US Top business headlines
    url_us = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsAPI_KEY}"
    data_us = requests.get(url_us)
    result_us = data_us.json()
    articles_us = result_us['articles']

    # UK Top business headlines
    url_uk = f"https://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey={newsAPI_KEY}"
    data_uk = requests.get(url_uk)
    result_uk = data_uk.json()
    articles_uk = result_uk['articles']

    # HU Top business headlines
    url_hu = f"https://newsapi.org/v2/top-headlines?country=hu&category=business&apiKey={newsAPI_KEY}"
    data_hu = requests.get(url_hu)
    result_hu = data_hu.json()
    articles_hu = result_hu['articles']

    return render_template("main.html", articles_us=articles_us, articles_uk=articles_uk, articles_hu=articles_hu)


@app.route("/science")
def science():
    """This function will return top science headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=science&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route("/entertainment")
def entertainment():
    """This function will return top entertainment headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=entertainment&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route("/sports")
def sports():
    """This function will return top sports headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=sports&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


@app.route('/general')
def general():
    """This function will return top general headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("main.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
