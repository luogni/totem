from flask.ext.security import UserMixin, RoleMixin
from totem import db


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


totems_users = db.Table('totems_users',
                        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                        db.Column('totem_id', db.String(), db.ForeignKey('totem.id')))


class Totem(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    type = db.Column(db.String(255))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    totems = db.relationship('Totem', secondary=totems_users, backref=db.backref('users', lazy='dynamic'))
    connections = db.relationship('Connection', backref=db.backref('user', lazy='joined'), cascade="all")


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)
