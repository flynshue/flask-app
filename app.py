import os, socket
from flask import Flask, render_template

app = Flask(__name__)

app_name = os.getenv('APP_NAME', 'flask app')
host = os.getenv('HOSTNAME', socket.gethostname())

pages = ["about", "docs"]

@app.route("/")
def home():
    return render_template("home.html", app_name=app_name, host_name=host, pages=pages)

@app.route("/about")
def about():
    return render_template("about.html", app_name=app_name, pages=pages)

@app.route("/docs")
def docs():
    return render_template("docs.html", app_name=app_name, pages=pages)