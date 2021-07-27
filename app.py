# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for
import bcrypt

app = Flask(__name__)
app.secret_key='_5#y2L"F4Q8z\n\xec]/'

app.config['MONGO_DBNAME'] = 'finalproject'

app.config['MONGO_URI'] = 'mongodb+srv://admin:J3gDjf-_izcxQ2W@cluster0.o1mo9.mongodb.net/finalproject?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",time=datetime.now())

@app.route('/signup', methods = ['GET','POST'])
def signup():
    # Are they posting with the form?
    if request.method == 'POST':
        # Connect to database
        users = mongo.db.users
        # Do something with the database - Does anyone have this name?
        existing_user = users.find_one({'name': request.form['username']})
                # Does user not exist? Add to the database!
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : str(hashpass, 'utf-8')})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'The username already exists'
    return render_template('signup.html')
@app.route ('/login', methods=["POST"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if bcrypt.hashpw((request.form['password']).encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username/password combination'
    # LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

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

    






    
    



