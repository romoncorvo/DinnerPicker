import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import random

from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///recommendations.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Allows the user to randomly get a suggestion for dinner""" 
    if request.method == "POST":
        dishesId = db.execute("SELECT id FROM recipes WHERE user_id = ?", session["user_id"])
        id = random.choice(dishesId)['id']

        recipe = db.execute("SELECT * FROM recipes WHERE user_id = ? AND id = ? ", session["user_id"], id)[0]

        ingredients = recipe['ingredients'].split("<\/>")
        method = recipe['method'].split("<\/>")
        dish = recipe['dish_name']

        return render_template("index.html", dish=dish, ingredients=ingredients, method=method)
    return render_template("index.html")


@app.route("/addRecipe", methods=["GET", "POST"])
@login_required
def addRecipe():
    """Allows the user to add a recipe to the database""" 
    if request.method == "POST":
        dish = request.form.get("dishName")

        i = 1
        ingredients = []
        while (ingredient := request.form.get("ingredient" + str(i))):
            ingredients.append(ingredient)
            i += 1

        i = 1
        method = []
        while (step := request.form.get("step" + str(i))):
            method.append(step)
            i += 1

        ingredients = "<\/>".join(ingredients)
        method = "<\/>".join(method)
        
        db.execute("INSERT INTO recipes (user_id, dish_name, ingredients, method) VALUES(?, ?, ?, ?)", session["user_id"], dish, ingredients, method)
        return render_template("addRecipe.html")
    return render_template("addRecipe.html")

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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted
        user = request.form.get("username")
        if not user:
            return apology("Please input a username")

        # Ensures username doesn't exist
        rows = db.execute("SELECT * FROM users WHERE username = ?", user)
        if len(rows) == 1:
            return apology("Username already exists")

        # Ensure password was submitted
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password or not confirmation:
            return apology("Please input a password and a confirmation")
        # Ensure password matches confirmation
        if not (password == confirmation):
            return apology("Password and confirmation do not match")

        #hash password
        hash = generate_password_hash(password)

        # Register user
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", user, hash)
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("register.html")


@app.route("/password", methods=["GET", "POST"])
@login_required
def changePassword():
    """Allows the user to change password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("oldPassword"):
            return apology("must provide current password", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide new password", 403)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("oldPassword")):
            return apology("invalid password", 403)

        # Ensure password was submitted
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password or not confirmation:
            return apology("Please input a password and a confirmation")
        # Ensure password matches confirmation
        if not (password == confirmation):
            return apology("Password and confirmation do not match")

        #hash password
        hash = generate_password_hash(password)

        # Register user
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("password.html")