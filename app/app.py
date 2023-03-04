import os
import requests
from flask import Flask, render_template, request, session


app = Flask("Your o News", static_folder='./app/static', template_folder='./app/templates')

newsAPI_KEY = os.environ.get('newsAPI_KEY')

app.config['SECRET_KEY'] = os.environ.get('SESSION_KEY')


@app.route("/")
def home():
    """
    Home page route
    """
    # US NEWS
    url_us = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsAPI_KEY}"
    data_us = requests.get(url_us)
    result_us = data_us.json()
    articles_us = result_us['articles']

    # UK NEWS
    url_uk = f"https://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey={newsAPI_KEY}"
    data_uk = requests.get(url_uk)
    result_uk = data_uk.json()
    articles_uk = result_uk['articles']

    # HU NEWS
    url_hu = f"https://newsapi.org/v2/top-headlines?country=hu&category=business&apiKey={newsAPI_KEY}"
    data_hu = requests.get(url_hu)
    result_hu = data_hu.json()
    articles_hu = result_hu['articles']

    return render_template("home.html", articles_us=articles_us, articles_uk=articles_uk, articles_hu=articles_hu)


@app.route("/news", methods=["GET"])
def news():
    """
    This function takes in an interest and a country and returns the top 5 news articles related to the interest in the country
    """
    country = request.args.get('country')
    interest = request.args.get('interest')
    interest = interest.lower()

    # get interest_list from session, or use an empty list if it's not in the session
    interest_list = session.get('interest_list', [])

    if country:
        # update country in session
        session['country'] = country

    if interest:
        # add interest to interest_list in session
        interest_list.append(interest)
        session['interest_list'] = interest_list

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("news.html", articles=articles, interest_list=interest_list)


if __name__ == "__main__":
    app.run(debug=True)
