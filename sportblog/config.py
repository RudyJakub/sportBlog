from dotenv import load_dotenv, dotenv_values
import os


load_dotenv(".env")
env = dict(dotenv_values())


class Config:
    SECRET_KEY = env.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    """
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    """
