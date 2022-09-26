from flask import Flask
from .extensions import database, migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
    migrate.init_app(app)

    return app