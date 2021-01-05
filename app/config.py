"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = True

    CACHE_DEFAULT_TIMEOUT = 300
    SQLALCHEMY_DATABASE_URI = "sqlite:////datastore/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CREDENTIAL = "YOUR_GOOGLE_CREDENTIAL"

    LINE_DOSCG_ADMIN_KEY = "<YOUR_LINE_ADMIN_GROUP_ID>"
    LINE_DOSCG_ACCESS_TOKEN = "<YOUR_CHANNEL_ACCESS_TOKEN>"
    LINE_DOSCG_CHANNEL_SECRET = "<YOUR_CHANNEL_SECRET>"
