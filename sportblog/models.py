from distutils.log import error
from email.policy import default
from xmlrpc.client import Boolean
from flask import current_app
from sportblog import db, login_manager, bcrypt
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_editor = db.Column(db.Boolean, nullable=False, default=False)
    articles = db.relationship('Article', backref='author', lazy=True)

    @staticmethod
    def create(username, email, password):
        if User.query.filter_by(username=username).first():
            raise Exception('Username already taken')
        if User.query.filter_by(email=email).first():
            raise Exception('Email already taken')
        hashed_password = hashed_password = bcrypt.\
        generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def set_editor_role(self, is_editor: bool):
        self.is_editor = is_editor
        db.session.commit()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def create(title, content, editor):
        article = Article(title=title, content=content, editor_id=editor)
        db.session.add(article)
        db.session.commit()

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
