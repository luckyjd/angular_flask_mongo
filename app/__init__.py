from flask import Flask
from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
from pymongo import MongoClient
# from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
app.debug = True
db = MongoClient('localhost', 27017).viettel
# db = MongoAlchemy(app)
# migrate = Migrate(app, db)
#login = LoginManager(app)
#login.login_view = 'login'


from app import routes, models
