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


@app.route("/health", methods=["GET"])
def health():
    """This function will return top health headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=health&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/health/countries', methods=["GET"])
def health_countries():
    """This function will return top health headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=health&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


@app.route('/technology', methods=["GET"])
def technology():
    """This function will return top technology headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=technology&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/technology/countries', methods=["GET"])
def technology_countries():
    """This function will return top technology headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=technology&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


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
def business_countries():
    """
    This function takes in an interest and a country and returns the top 5 news articles related to the interest in the country
    """
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


@app.route("/science", methods=["GET"])
def science():
    """This function will return top science headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=science&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/science/countries', methods=["GET"])
def sciene_countries():
    """This function will return top science headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=science&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


@app.route("/entertainment", methods=["GET"])
def entertainment():
    """This function will return top entertainment headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=entertainment&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/entertainment/countries', methods=["GET"])
def entertainment_countries():
    """This function will return top entertainment headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=entertainment&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


@app.route("/sports", methods=["GET"])
def sports():
    """This function will return top sports headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=sports&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/sports/countries', methods=["GET"])
def sports_countries():
    """This function will return top sports headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=sports&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


@app.route('/general', methods=["GET"])
def general():
    """This function will return top general headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles)


@app.route('/general/countries', methods=["GET"])
def general_countries():
    """This function will return top general headlines from the country user selected"""
    country = request.args.get('country')
    if country:
        session['country'] = country

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=general&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("countries.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
