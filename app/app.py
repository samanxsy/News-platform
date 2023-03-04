import os
import requests
from flask import Flask, render_template, request, session


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

    return render_template("home.html", articles=articles)


@app.route("/search", methods=["GET"])
def search():
    """This function will return the content user searched for"""
    search = request.args.get('search')
    if search:
        search = search.replace(" ", "+")

    url = f"https://newsapi.org/v2/everything?q={search}&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route("/business", methods=["GET"])
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

    return render_template("business.html", articles_us=articles_us, articles_uk=articles_uk, articles_hu=articles_hu)


@app.route("/business/countries", methods=["GET"])
def business_country():
    """
    This function takes in an interest and a country and returns the top 5 news articles related to the interest in the country
    """
    country = request.args.get('country')
    if country:
        # update country in session
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
