from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
if os.getenv("DEBUG") == 0: #DEBUG = variável de ambiente no render
    link_banco = os.getenv("DATABASE_URL") #no ambiente online do render
else:
    link_banco = "sqlite:///comunidade.db" #banco de dados usado fora do render
app.config["SQLALCHEMY_DATABASE_URI"] = link_banco
app.config["SECRET_KEY"] = "3502e6628320556d15305267639bd81a"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from fakepinterest import routes