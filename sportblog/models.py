import string
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

    def __init__(self, username: str, email: str, password: str, is_editor=False):
        super().__init__()
        if User.query.filter_by(username=username).first():
            raise Exception('Username already taken')
        if User.query.filter_by(email=email).first():
            raise Exception('Email already taken')
        self.username = username
        self.email = email
        self.password = self._generate_password_hash(password)
        self.is_editor = is_editor

    @staticmethod
    def _generate_password_hash(password: str):
        hashed_password = bcrypt.\
        generate_password_hash(password).decode('utf-8')
        return hashed_password

    def set_editor_role(self, is_editor: bool):
        self.is_editor = is_editor
        db.session.commit()

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', Editor: {self.is_editor})"


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title: str, content: str, editor: User):
        super().__init__()
        self.title = title
        self.content = content
        self.editor_id = editor.id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', Editor: {self.editor_id})"
