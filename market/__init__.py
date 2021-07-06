from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '4c0a5780516ade6e9804c12b'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes