# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/survey", methods = ["GET","POST"])
def survey():
    if request.method=="GET":
        return render_template("survey.html")
    else:
        skin=request.form["skin"]
        print (skin)
        if skin=="oily":
            return render_template("oily.html")
        if skin=="dry":
            return render_template("dry.html")
        if skin=="combination":
            return render_template("combination.html")
        if skin=="sensitive":
            return render_template("sensitive.html")

    






    
    



