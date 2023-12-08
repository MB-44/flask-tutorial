from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# # use os.environment to access enviornment variables
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','default_secret_key')

posts = [
    {
        "author": "Menath Baddegana",
        "title": "Blog Post 01",
        "content": "First post content",
        "datePosted": "April 21, 2022"
    },
    {
        "author": "Amandi sadara",
        "title": "Blog Post 02",
        "content": "Second post content",
        "datePosted": "November 76, 2023"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title = "Home", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title = "About")


if __name__ == "__main__":
    app.run(debug=True)