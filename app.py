from flask import Flask,render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ =="__main__":
    app.run(debug=True)
