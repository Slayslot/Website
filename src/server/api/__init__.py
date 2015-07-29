from flask import Flask
from flask.ext.admin import Admin
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences
from flask.ext.security import MongoEngineUserDatastore, Security
from os import environ
from flask.ext.security.utils import encrypt_password

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

db = MongoEngine()
admin = Admin(name="MozillaDelhi API")
app.secret_key = environ['SECRET_KEY']

app.config['MONGODB_SETTINGS'] = {'DB': environ['DB'], 'HOST': environ['HOST']}
app.config['SECURITY_PASSWORD_HASH'] = environ['SECURITY_PASSWORD_HASH']
app.config['SECURITY_PASSWORD_SALT'] = environ['SECURITY_PASSWORD_SALT']

db.init_app(app)
admin.init_app(app)

from api import models
from api import views
from api import administration

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)