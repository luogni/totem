from totem import app, db, user_datastore
from flask import Flask, send_from_directory, render_template
import os.path
from flask.ext.security import login_required


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


@app.route("/")
@login_required
def index():
    return render_template('index.html')
