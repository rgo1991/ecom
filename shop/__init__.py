from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder='templates')
#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'asdasdjowehr3irwr'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

from shop.admin import routes
from shop.products import routes
