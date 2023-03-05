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

    # Top headlines
    url = f"https://newsapi.org/v2/everything?q={search}&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    # Tech news
    url_tech = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={newsAPI_KEY}"
    data_tech = requests.get(url_tech)
    result_tech = data_tech.json()
    articles_tech = result_tech['articles']

    # Health news
    url_health = f"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={newsAPI_KEY}"
    data_health = requests.get(url_health)
    result_health = data_health.json()
    articles_health = result_health['articles']

    return render_template("home.html", articles=articles, articles_tech=articles_tech, articles_health=articles_health)


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
    url = f"https://newsapi.org/v2/top-headlines?country=&category=health&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route('/technology', methods=["GET"])
def technology():
    """This function will return top technology headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=technology&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/business")
def business():
    """
    This function will return top business headlines from US, UK and Hungary
    """
    # US Top business headlines
    url = f"https://newsapi.org/v2/top-headlines?country=&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/science")
def science():
    """This function will return top science headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=science&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/entertainment")
def entertainment():
    """This function will return top entertainment headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=entertainment&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route("/sports")
def sports():
    """This function will return top sports headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=sports&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


@app.route('/general')
def general():
    """This function will return top general headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("common.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
