import os
import secrets

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy.orm import sessionmaker
from helpers import apology, login_required, lookup
from modules import Base, History, Owned_stock, Users, engine

#admin users name
admin = ["Shunto", "Shunto50", "Test_Shunto"]

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Create Session
orm_Session = sessionmaker(bind=engine)
orm_session = orm_Session()
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

#Secret key
secret = secrets.token_urlsafe(32)
app.secret_key = secret

# Make sure Microsoft BingAPI key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# 
@app.route("/")
def top():
    if session["name"]:
        return redirect("index")
    else:
        return render_template("topmessage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        with orm_session as ss:
            rows = ss.query(Users).filter(Users.username == request.form.get("username")).all()
            ss.close()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0].hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0].id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/index")
@login_required
def index():

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    # If the request method is GET render to register.html"""
    if request.method == "GET":
        # render template"""
        return render_template("register.html")
    # If the request method is POST"""
    else:
        # Check form content"""
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # If user name is blank render to apology"""
        if not username:
            return apology("Fill username")
        # If username is not unique render to apology"""
        with orm_session as ss:
            rows = ss.query(Users).filter(Users.username == username).all()
        if len(rows) != 0:
            return apology("The username already exists")
        
        # if either of passwords is blank render apology
        if not password or not confirmation:
            return apology("Password is blank")
        
        # if password =! confirmation render to apology"""
        elif password != confirmation:
            return apology("Password doesn't match")
        # hash the password"""
        hashed_pw = generate_password_hash(password)
        # store date from form to db"""
        with orm_session as ss:
            if not username in admin
                new_user = Users(Users.username == username, Users.hash == hashed_pw)
            else:
                new_user = Users(Users.username == username, Users.hash == hashed_pw, Users.image_search == 1000)
            ss.add(new_user)
            ss.commint()
        # render to login?"""
        message = "You are registered! You can login now."
        return render_template("index.html", message=message)

@app.route("add", methods = ["POST", "GET"])
def add():


@app.route("")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)



#Initiating database
def init_db():
    try:
        Base.metadata.drop_all(engine)
    except Exception as e:
        print("drop error! but continue")
    Base.metadata.create_all(engine)
    print("create all is done")

# initiate app

if __name__ == "__main__":
    app.run()
