from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '44cb08adee3c79c23ce4583c'
db = SQLAlchemy(app) # Database
bcrypt = Bcrypt(app) # Password encryption on database
login_manager = LoginManager(app) # Applying login logic
login_manager.login_view = "login_page"
login_manager.login_message_category = "info" # Turns message into a flash message 
from shop import routes

