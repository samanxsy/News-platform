import os
import requests
from flask import Flask, render_template, request, session
import app.common.countries as countries


app = Flask("YourO News", static_folder='./app/static', template_folder='./app/templates')
newsAPI_KEY = os.environ.get('newsAPI_KEY')
app.secret_key = os.environ.get('SESSION_KEY')

DEFAULT_COUNTRY = "us"
app.config["DEFAULT_COUNTRY"] = DEFAULT_COUNTRY
countries = countries.countries


@app.route("/")
def home():
    """This function will return the home page where the user can search about any topic"""

    # Top headlines
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles'][0:3]

    # Tech news
    url_tech = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={newsAPI_KEY}"
    data_tech = requests.get(url_tech)
    result_tech = data_tech.json()
    articles_tech = result_tech['articles'][0:3]

    url_business = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsAPI_KEY}"
    data_business = requests.get(url_business)
    result_business = data_business.json()
    articles_business = result_business['articles'][0:3]

    # Health news
    url_health = f"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={newsAPI_KEY}"
    data_health = requests.get(url_health)
    result_health = data_health.json()
    articles_health = result_health['articles'][0:3]

    return render_template("home.html", articles=articles, articles_tech=articles_tech, articles_health=articles_health, articles_business=articles_business)


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

    return render_template("common.html", articles=articles)


@app.route("/health")
def health():
    """This function will return top health headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles, countries=countries)


@app.route('/technology', methods=["GET"])
def technology():
    """This function will return top technology headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=technology&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/business")
def business():
    """
    This function will return top business headlines from US, UK and Hungary
    """
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/science")
def science():
    """This function will return top science headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=science&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/entertainment")
def entertainment():
    """This function will return top entertainment headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/sports")
def sports():
    """This function will return top sports headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route('/general')
def general():
    """This function will return top general headlines"""
    country = session.get('country', DEFAULT_COUNTRY)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
