from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return "<p>Hello, Stink Blog face!</p>"
@app.route("/about_me.html")
def about():
    return render_template('about_me.html')