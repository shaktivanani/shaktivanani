from flask import Flask,render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)




@app.route("/")
def hello_world():
   return render_template("index.html",)


if __name__ =="__main__":
    app.run(debug=True)
