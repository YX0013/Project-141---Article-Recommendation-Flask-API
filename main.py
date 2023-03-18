from flask import Flask, jsonify, request
from flask_cors import CORS
import csv

all_articles = []
liked_articles = []
disliked_articles = []
unwatched_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)
CORS(app)

@app.route("/get-article")
def get_article():
    global all_articles
    return jsonify({
        "data": all_articles[0],
        "message": "success"
    }), 200

@app.route("/liked-article", methods = ["POST"])
def liked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "message": "success"
    }), 200

@app.route("/disliked-article", methods = ["POST"])
def disliked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "message": "success"
    }), 200

@app.route("/unwatched-article", methods = ["POST"])
def unwatched_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    unwatched_articles.append(article)
    return jsonify({
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run(debug = True)