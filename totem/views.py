from totem import app, db, user_datastore, social
from flask import send_from_directory, render_template
import os.path
from flask.ext.security import login_required
from flask.ext.social.utils import get_connection_values_from_oauth_response
from flask.ext.social import login_failed
from flask.ext.login import login_user
from flask.ext.social.views import connect_handler


@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='luca.ognibene@gmail.com', password='test')
    db.session.commit()
                

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    user = user_datastore.create_user(email=None, password="pippo")
    user_datastore.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    user_datastore.commit()
    return render_template('index.html')


@app.route("/")
@login_required
def index():
    return render_template('index.html',
                           facebook_conn=social.facebook.get_connection())
