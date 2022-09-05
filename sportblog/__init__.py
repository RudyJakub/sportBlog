from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# from flask_mail import Mail
from sportblog.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)

    from sportblog.blog.routes import blog
    from sportblog.editor_site.routes import editor_site
    from sportblog.auth.routes import auth
    from sportblog.errors.handlers import errors
    app.register_blueprint(blog, url_prefix='')
    app.register_blueprint(editor_site, url_prefix='/editor_site')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(errors)
    
    return app


def create_database(app):
    app_context = app.app_context()
    app_context.push()
    db.create_all(app=app)


def create_new_editor(app):
    app_context = app.app_context()
    app_context.push()
    from sportblog.models import User
    email = input('Email: ')
    username = input('Username: ')
    password = input('Password: ')

    new_editor = User(
        email=email,
        username=username,
        password=password
    )

    new_editor.set_editor_role(True)

    print("Succesfully created new editor")
