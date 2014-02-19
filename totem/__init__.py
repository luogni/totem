from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
import flask.ext.social.providers.facebook
flask.ext.social.providers.facebook.config['request_token_params'] = {'scope': 'email,user_location'}
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.assets import Environment

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='lutotem-key-123321', SQLALCHEMY_DATABASE_URI='sqlite://',
                  SOCIAL_FACEBOOK={'consumer_key': '283811785104353',
                                   'consumer_secret': '1459afa7e3c9f55c499694f9f71781f0'})
db = SQLAlchemy(app)
assets = Environment(app)

from totem.models import User, Role, Connection

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

import totem.views  # noqa
import totem.assets  # noqa
