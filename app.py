import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
#from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///recomendations.db")