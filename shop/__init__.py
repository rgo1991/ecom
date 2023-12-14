from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')
#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////myshop.db'
db = SQLAlchemy(app)

from shop import routes
