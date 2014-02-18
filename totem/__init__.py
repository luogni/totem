from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='lutotem-key-123321', SQLALCHEMY_DATABASE_URI='sqlite://')
db = SQLAlchemy(app)

import totem.models

user_datastore = SQLAlchemyUserDatastore(db, totem.models.User, totem.models.Role)
security = Security(app, user_datastore)

import totem.views