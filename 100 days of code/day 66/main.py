from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    pass


@app.route("/add")
def add():
    pass

@app.route("/random", methods=["GET"])
def get_random_cafe():
  pass

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)


if __name__ == "__main__":
    app.run(debug=True)

