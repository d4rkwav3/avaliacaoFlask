from flask import Flask
from .extensions import database, migrate
from .routes.home import home
from .routes.new import new
from .routes.list import list_clients
from .routes.appointment import aptm
from .setup_db import create_database
import os


def create_app():
    caminho = os.path.abspath(os.getcwd())+"/db.sqlite3"
    try:
        dbase = open(caminho, "r")
        dbase.close()
    except FileNotFoundError:
        q = input("Nenhuma base de dados localizada, deseja criar uma nova? ('S'im/'N'ão)\n")

        if q == 'S' or q == 's' or q == "Sim" or q == "sim":
            create_database()
        else:
            print("Não é possível continuar sem uma base de dados, por favor verifique e tente novamente.")

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(new)
    app.register_blueprint(list_clients)
    app.register_blueprint(aptm)

    return app
