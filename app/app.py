import os
import requests
from flask import Flask, render_template, request


app = Flask("Your o News", static_folder='./app/static', template_folder='./app/templates')

newsAPI_KEY = os.environ.get('newsAPI_KEY')

app.config['SECRET_KEY'] = os.environ.get('SESSION_KEY')

interest_list = []


@app.route("/")
def home():
    """Home page route"""
    return render_template("home.html")


@app.route("/news", methods=["GET"])
def news():
    """This function takes in an interest and a country and returns the top 5 news articles related to the interest in the country."""
    country = request.args.get('country')
    interest = request.args.get('interest')
    interest = interest.lower()
    interest_list.append(interest)

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()
    articles = result['articles']

    return render_template("home.html", articles=articles, interest_list=interest_list)


if __name__ == "__main__":
    app.run(debug=True)
