from flask import Flask, render_template

app = Flask("Your o News", static_folder='./app/static', template_folder='./app/templates')


@app.route("/")
def home():
    return render_template("home.html")
