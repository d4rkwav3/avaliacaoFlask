from flask import Flask
from .extensions import database, migrate
from .routes.home import home
from .routes.new import new
from .routes.list import list_clients
from .setup_db import create_database


def create_app():
    try:
        dbase = open("./avaliaçãoFlask/db.sqlite3", "r")
        dbase.close()
    except FileNotFoundError:
        create_database()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(new)
    app.register_blueprint(list_clients)

    return app