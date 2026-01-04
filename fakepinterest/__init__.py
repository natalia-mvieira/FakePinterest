from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv["SQLALCHEMY_DATABASE_URI"]
app.config["SECRET_KEY"] = os.getenv["SECRET_KEY"]
app.config["UPLOAD_FOLDER"] = os.getenv["UPLOAD_FOLDER"]

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from fakepinterest import routes
