from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


from app import server
# from app import views
from app import models
